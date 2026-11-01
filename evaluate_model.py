
import csv
import json
from pathlib import Path

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


# -------------------------------
# 1. Dataset paths
# -------------------------------
DATASET_DIR = Path(r"D:\DeepLearning\archive")
IMAGE_DIR = DATASET_DIR / "Images"
CAPTION_FILE = DATASET_DIR / "captions.txt"

MODEL_ID = "Salesforce/blip-image-captioning-base"
NUM_IMAGES = 100


# -------------------------------
# 2. Validate dataset paths
# -------------------------------
if not IMAGE_DIR.is_dir():
    raise FileNotFoundError(f"Image folder not found: {IMAGE_DIR}")

if not CAPTION_FILE.is_file():
    raise FileNotFoundError(f"Caption file not found: {CAPTION_FILE}")


# -------------------------------
# 3. Load reference captions
# -------------------------------
references = {}

with CAPTION_FILE.open(
    "r", encoding="utf-8-sig", newline=""
) as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip header: image,caption

    for row in reader:
        if len(row) < 2:
            continue

        filename = row[0].strip()
        caption = row[1].strip()

        if filename and caption:
            references.setdefault(filename, []).append(caption)


# -------------------------------
# 4. Select evaluation images
# -------------------------------
samples = [
    (filename, captions)
    for filename, captions in references.items()
    if (IMAGE_DIR / filename).is_file()
][:NUM_IMAGES]

print("Images with reference captions:", len(references))
print("Images selected for evaluation:", len(samples))

if not samples:
    raise RuntimeError(
        "No matching images found. Check the dataset paths and filenames."
    )


# -------------------------------
# 5. Load pretrained BLIP model
# -------------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

print("\nLoading BLIP model...")
print("Device:", device)

processor = BlipProcessor.from_pretrained(MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)

model.to(device)
model.eval()

print("Model loaded successfully.")


# -------------------------------
# 6. Generate and record captions
# -------------------------------
results = []
errors = []

for index, (filename, captions) in enumerate(samples, start=1):
    image_path = IMAGE_DIR / filename

    try:
        with Image.open(image_path) as image:
            image = image.convert("RGB")
            inputs = processor(
                images=image,
                return_tensors="pt"
            ).to(device)

        with torch.inference_mode():
            output = model.generate(
                **inputs,
                max_new_tokens=30,
                do_sample=False,
                num_beams=1,
            )

        generated = processor.decode(
            output[0],
            skip_special_tokens=True
        ).strip()

        print(f"\n[{index}/{len(samples)}] {filename}")
        print("Generated:", generated)
        print("Reference captions:")

        for caption in captions:
            print("-", caption)

        if generated:
            results.append({
                "image": filename,
                "generated_caption": generated,
                "reference_captions": captions,
            })
        else:
            errors.append({
                "image": filename,
                "error": "No caption generated",
            })

    except Exception as error:
        print(f"\n[{index}/{len(samples)}] ERROR: {filename}")
        print(f"{type(error).__name__}: {error}")

        errors.append({
            "image": filename,
            "error": f"{type(error).__name__}: {error}",
        })


# -------------------------------
# 7. Save evaluation results
# -------------------------------
OUTPUT_FILE = Path("evaluation_results.json")

with OUTPUT_FILE.open("w", encoding="utf-8") as file:
    json.dump(results, file, indent=2, ensure_ascii=False)

print("\n-------------------------------")
print("Evaluation run completed")
print("Images selected:", len(samples))
print("Captions generated:", len(results))
print("Errors:", len(errors))
print("Results saved to:", OUTPUT_FILE.resolve())

if errors:
    print("\nImages with errors:")
    for item in errors:
        print("-", item["image"], ":", item["error"])
