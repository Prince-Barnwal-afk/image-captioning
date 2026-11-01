
from pathlib import Path
import csv

DATASET_DIR = Path(r"D:\DeepLearning\archive")
IMAGE_DIR = DATASET_DIR / "Images"
CAPTION_FILE = DATASET_DIR / "captions.txt"

# Find the caption file if its extension differs
if not CAPTION_FILE.exists():
    matches = list(DATASET_DIR.glob("captions*"))
    if matches:
        CAPTION_FILE = matches[0]

print("Image folder exists:", IMAGE_DIR.is_dir())
print("Caption file:", CAPTION_FILE)
print("Caption file exists:", CAPTION_FILE.is_file())

if IMAGE_DIR.is_dir():
    images = list(IMAGE_DIR.glob("*.jpg"))
    print("JPG images found:", len(images))

if CAPTION_FILE.is_file():
    with CAPTION_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        for _, row in zip(range(6), reader):
            print(row)
