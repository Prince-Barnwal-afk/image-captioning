# Image Captioning with BLIP

A deep-learning application that generates natural-language captions for uploaded images using the pretrained BLIP (Bootstrapping Language-Image Pre-training) model and a Streamlit web interface.

## Features

- Upload images in JPG, JPEG, or PNG format.
- Generate English captions using a pretrained BLIP model.
- Display the uploaded image and its generated caption.
- Automatically select CUDA when available; otherwise, use the CPU.
- Cache the loaded model while the Streamlit application is running.

## Technology Stack

- Python
- PyTorch
- Hugging Face Transformers
- Salesforce BLIP Image Captioning Base
- Pillow
- Streamlit

## Project Structure

```text
image-captioning/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

- Python 3.10 or a compatible newer Python version supported by the dependencies.
- Git
- An internet connection for installing dependencies and downloading the pretrained model on the first run.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/image-captioning.git
cd image-captioning
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

### 3. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

PyTorch may use the CPU or a compatible CUDA GPU, depending on the installed build and available hardware.

### 5. Run the application

```powershell
python -m streamlit run app.py
```

Open the local URL printed in the terminal, usually:

```text
http://localhost:8501
```

## Downloading the Pretrained Model

The application uses:

`Salesforce/blip-image-captioning-base`

The model and processor are downloaded automatically through Hugging Face Transformers when the application first loads them. An internet connection is required for the initial download. The downloaded files are cached locally for subsequent runs.

The model does not need to be downloaded manually or committed to this Git repository.

## How to Use

1. Start the Streamlit application.
2. Upload a JPG, JPEG, or PNG image.
3. Click **Generate Caption**.
4. Wait for inference to finish.
5. Read the generated caption displayed on the page.

## Performance Notes

- The first run may take longer because the pretrained model must be downloaded and loaded.
- CPU inference can be slower than inference on a compatible GPU.
- The application caches the loaded model while the Streamlit process remains active.
- Generated captions may omit details or incorrectly describe an image.

## Troubleshooting

### Python or pip is not recognized

Install Python and ensure it is available on your system PATH. Restart the terminal and verify:

```powershell
python --version
python -m pip --version
```

### Streamlit cannot find `app.py`

Ensure the terminal is inside the project directory:

```powershell
cd path\to\image-captioning
dir
```

Confirm that `app.py` is listed, then run the Streamlit command again.

### Model download fails

Check your internet connection and rerun the application. The initial model download requires access to Hugging Face.

### The application is slow

CPU-based model inference can take time. Keep the terminal running while using the application.

## Current Project Status

The basic Streamlit interface and pretrained BLIP caption-generation workflow have been implemented and tested locally. Dataset-based evaluation, quantitative performance analysis, and online deployment are separate project milestones.

## License and Attribution

This project uses the pretrained BLIP model provided by Salesforce through Hugging Face Transformers. Check the model card and applicable licenses before redistributing model files or deploying the application commercially.

Model: https://huggingface.co/Salesforce/blip-image-captioning-base

Transformers: https://huggingface.co/docs/transformers

Streamlit: https://docs.streamlit.io/
(Get-Item .\README.md).Length