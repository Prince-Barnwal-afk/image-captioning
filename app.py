
import streamlit as st
import torch
from PIL import Image, ImageOps
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
)

MODEL_ID = "Salesforce/blip-image-captioning-base"


@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    processor = BlipProcessor.from_pretrained(MODEL_ID)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)

    model.to(device)
    model.eval()

    return processor, model, device


st.set_page_config(
    page_title="Image Captioning",
    page_icon="🖼️",
    layout="centered",
)

st.title("Image Captioning with BLIP")
st.write("Upload a photograph to generate an English caption.")
st.caption("This application uses a pretrained model. Captions may be incorrect.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    try:
        image = ImageOps.exif_transpose(
            Image.open(uploaded_file)
        ).convert("RGB")

        st.image(image, caption="Uploaded image", width="stretch")

        if st.button("Generate Caption", type="primary"):
            with st.spinner("Loading model and generating caption..."):
                processor, model, device = load_model()

                inputs = processor(
                    images=image,
                    return_tensors="pt",
                ).to(device)

                with torch.inference_mode():
                    output = model.generate(
                        **inputs,
                        max_new_tokens=30,
                        do_sample=False,
                        num_beams=1,
                    )

                caption = processor.decode(
                    output[0],
                    skip_special_tokens=True,
                ).strip()

            if caption:
                st.subheader("Generated Caption")
                st.success(caption)
            else:
                st.warning("No caption was generated.")

    except Exception as error:
        st.error("Image processing or caption generation failed.")
        print(type(error).__name__, str(error))
