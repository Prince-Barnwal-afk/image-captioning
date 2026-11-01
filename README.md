# Image Captioning with BLIP

A deep-learning application that generates natural-language captions for uploaded images using the pretrained BLIP (Bootstrapping Language-Image Pre-training) model and a Streamlit web interface.

## Features

- Upload images in JPG, JPEG, or PNG format.
- Generate English captions using a pretrained BLIP model.
- Display the uploaded image and its generated caption.
- Automatically use CUDA when available; otherwise, use the CPU.
- Cache the loaded model during the Streamlit session.
- Evaluate generated captions against human-written reference captions from Flickr8k.
- Calculate BLEU-4 scores for quantitative evaluation.

## Technology Stack

- Python
- PyTorch
- Hugging Face Transformers
- Salesforce BLIP Image Captioning Base
- Pillow
- Streamlit
- NLTK for BLEU evaluation

## Project Structure

```text
image-captioning/
├── app.py
├── check_dataset.py
├── evaluate_model.py
├── calculate_metrics.py
├── evaluation_results.json
├── evaluation_summary.md
├── test_results.md
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

- Python 3.10 or a compatible newer version supported by the dependencies.
- Git
- An internet connection for installing dependencies and downloading the pretrained model.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prince-Barnwal-afk/image-captioning.git
cd image-captioning
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Run the application

```powershell
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually:

http://localhost:8501

## Pretrained Model

The application uses:

`Salesforce/blip-image-captioning-base`

Hugging Face Transformers downloads the model and processor automatically when they are first loaded. The files are cached locally for subsequent runs. Do not commit model weights to the Git repository.

Model card: https://huggingface.co/Salesforce/blip-image-captioning-base

## How to Use the Application

1. Start the Streamlit application.
2. Upload a JPG, JPEG, or PNG image.
3. Click **Generate Caption**.
4. Wait for the model to generate a caption.
5. Read the caption displayed on the page.

## Dataset-Based Evaluation

The project uses the Flickr8k dataset to compare generated captions with human-written reference captions.

The dataset is stored locally and is not included in this repository.

Expected dataset structure:

```text
archive/
├── Images/
└── captions.txt
```

The evaluation scripts currently expect the dataset at:

`D:\DeepLearning\archive`

If the dataset is stored elsewhere, update `DATASET_DIR` in `check_dataset.py`, `evaluate_model.py`, and `calculate_metrics.py` as applicable.

### Evaluation Workflow

1. Run `check_dataset.py` to verify the dataset files and image-caption mappings.
2. Run `evaluate_model.py` to generate captions for the selected images and save the results to `evaluation_results.json`.
3. Run `calculate_metrics.py` to calculate BLEU-4 scores against the reference captions.

Run these commands from the project directory:

```powershell
python check_dataset.py
python evaluate_model.py
python calculate_metrics.py
```

The evaluation scripts require the Flickr8k dataset to be downloaded and configured locally.

## Initial Evaluation Results

The following results were obtained during the initial evaluation:

| Metric | Result |
|---|---:|
| Images evaluated | 100 |
| Captions generated | 100 |
| Generation errors | 0 |
| Corpus BLEU-4 | 0.1931 |

The model generated captions for all 100 selected images without reported errors. The BLEU-4 score measures n-gram overlap between generated captions and human-written references. It is not a percentage accuracy score.

These results are preliminary and apply only to the selected 100-image subset. A larger evaluation and manual review are needed to assess caption quality more comprehensively.

See `evaluation_summary.md` for the evaluation details and `evaluation_results.json` for the generated captions and saved results.

## Limitations

- Captions may omit important objects or visual details.
- The model may describe objects or actions incorrectly.
- BLEU-4 does not fully measure semantic correctness or factual accuracy.
- The reported evaluation uses only 100 images.
- CPU inference may be slower than inference on a compatible GPU.

## Troubleshooting

### Python or pip is not recognized

Install Python and ensure it is available on your system PATH. Restart the terminal and verify:

```powershell
python --version
python -m pip --version
```

### Streamlit cannot find `app.py`

Ensure the terminal is inside the project directory and that `app.py` is listed:

```powershell
cd path\to\image-captioning
dir
```

### Model download fails

Check your internet connection and try again. The initial download requires access to Hugging Face.

### Dataset files cannot be found

Check that the `Images` folder and `captions.txt` file exist at the location configured in the evaluation scripts.

### The application is slow

The first run downloads and loads the model. CPU inference may also take time.

## Project Status

- Streamlit application implemented and tested locally.
- Initial manual testing completed on five images.
- Flickr8k dataset configured locally.
- Automated caption generation completed for 100 images.
- BLEU-4 evaluation completed for the 100-image subset.
- Public deployment and broader evaluation remain future milestones.

## References

- BLIP model: https://huggingface.co/Salesforce/blip-image-captioning-base
- Hugging Face Transformers: https://huggingface.co/docs/transformers
- Streamlit documentation: https://docs.streamlit.io/
- Flickr8k dataset: https://www.kaggle.com/datasets/adityajn105/flickr8k


## Live Demo

Try the deployed application here:

**[Image Captioning with BLIP](https://image-captioninggit-jjsmemeek7wc33n9g8gkwcv.streamlit.app/)**

Upload a JPG, JPEG, or PNG image to generate an English caption using the pretrained BLIP model.