
import json
from pathlib import Path
import nltk
from nltk.translate.bleu_score import (
    corpus_bleu,
    sentence_bleu,
    SmoothingFunction,
)

RESULTS_FILE = Path("evaluation_results.json")

if not RESULTS_FILE.is_file():
    raise FileNotFoundError(
        f"Results file not found: {RESULTS_FILE.resolve()}"
    )

with RESULTS_FILE.open("r", encoding="utf-8") as file:
    results = json.load(file)

if not results:
    raise ValueError("No evaluation results found.")

references = []
hypotheses = []

smooth = SmoothingFunction().method1

for item in results:
    generated = item["generated_caption"].strip().lower()
    reference_captions = item["reference_captions"]

    if not generated or not reference_captions:
        continue

    # Tokenize captions into words
    reference_tokens = [
        nltk.word_tokenize(caption.lower())
        for caption in reference_captions
    ]
    generated_tokens = nltk.word_tokenize(generated)

    references.append(reference_tokens)
    hypotheses.append(generated_tokens)

    score = sentence_bleu(
        reference_tokens,
        generated_tokens,
        weights=(0.25, 0.25, 0.25, 0.25),
        smoothing_function=smooth,
    )

    print(f"\nImage: {item['image']}")
    print(f"Generated: {item['generated_caption']}")
    print(f"Sentence BLEU-4: {score:.4f}")

if hypotheses:
    overall_bleu = corpus_bleu(
        references,
        hypotheses,
        weights=(0.25, 0.25, 0.25, 0.25),
        smoothing_function=smooth,
    )

    print("\n-----------------------------")
    print("Evaluation summary")
    print("Images evaluated:", len(hypotheses))
    print(f"Corpus BLEU-4: {overall_bleu:.4f}")
    print("-----------------------------")
else:
    print("No valid caption pairs were available.")
