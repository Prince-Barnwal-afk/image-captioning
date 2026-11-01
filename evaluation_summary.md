# BLIP Image Captioning — Evaluation Summary

## Model
- Model: `Salesforce/blip-image-captioning-base`
- Framework: PyTorch and Hugging Face Transformers
- Dataset: Flickr8k

## Evaluation Setup
- Images selected: 100
- Captions generated successfully: 100
- Errors: 0
- Metric: Corpus BLEU-4
- Evaluation subset: First 100 matching images in the caption file

## Result

| Metric | Result |
|---|---:|
| Images evaluated | 100 |
| Successful generations | 100/100 |
| Errors | 0 |
| Corpus BLEU-4 | 0.1931 |

## Interpretation

The model generated captions for all selected images without reported errors. The Corpus BLEU-4 score measures n-gram overlap between generated captions and human-written reference captions. It is not a percentage accuracy score.

This result is preliminary because the evaluation uses only 100 images. Some generated captions may correctly identify the main subject while omitting details or describing the scene differently from the references.

## Limitations
- The evaluation subset contains only 100 images.
- BLEU measures text overlap and does not fully assess visual correctness.
- Further evaluation on a larger subset and manual inspection of caption quality are needed.
