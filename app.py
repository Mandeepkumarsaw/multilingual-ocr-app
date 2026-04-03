# ==========================================
# ADVANCED IMAGE/PDF TO TEXT EXTRACTOR (OCR)
# ==========================================

import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np
import fitz  # PyMuPDF
import io

# ==============================
# SET TESSERACT PATH (WINDOWS)
# ==============================
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# ==============================
# IMAGE PREPROCESSING FUNCTION
# ==============================
def preprocess_image(image):
    img = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise removal
    gray = cv2.medianBlur(gray, 3)

    # Thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return thresh


# ==============================
# OCR FUNCTION
# ==============================
def extract_text(image, lang='eng'):
    return pytesseract.image_to_string(image, lang=lang)


# ==============================
# PDF TO IMAGE FUNCTION
# ==============================
def pdf_to_images(uploaded_file):
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    images = []
    for page in doc:
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        images.append(img)

    return images


# ==============================
# STREAMLIT UI
# ==============================
st.set_page_config(page_title="OCR Tool", layout="centered")

st.title("🧠 Image & PDF to Text Extractor")
st.write("Supports English, Hindi & multi-page PDFs")

# Language selection
# Language selection with Indian languages
language_dict = {
    "English": "eng",
    "Hindi": "hin",
    "Bengali": "ben",
    "Tamil": "tam",
    "Telugu": "tel",
    "Marathi": "mar",
    "Gujarati": "guj",
    "Kannada": "kan",
    "Malayalam": "mal",
    "Punjabi": "pan",
    "Odia": "ori",
    "Urdu": "urd",
    "Sanskrit": "san",
    "English + Hindi": "eng+hin",
    "All Indian Languages": "eng+hin+ben+tam+tel+mar+guj+kan+mal+pan+ori+urd+san"
}

selected_lang = st.selectbox("🌐 Select Language", list(language_dict.keys()))
lang_option = language_dict[selected_lang]

# File upload
uploaded_file = st.file_uploader(
    "📤 Upload Image or PDF",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file is not None:
    file_type = uploaded_file.type
    all_text = ""

    # ==========================
    # IMAGE PROCESSING
    # ==========================
    if "image" in file_type:
        image = Image.open(uploaded_file)

        st.subheader("📷 Uploaded Image")
        st.image(image, use_column_width=True)

        processed = preprocess_image(image)

        st.subheader("⚙️ Processed Image")
        st.image(processed, clamp=True)

        text = extract_text(processed, lang_option)
        all_text += text

    # ==========================
    # PDF PROCESSING
    # ==========================
    elif "pdf" in file_type:
        st.subheader("📄 Processing PDF...")

        images = pdf_to_images(uploaded_file)

        for i, img in enumerate(images):
            st.write(f"Page {i+1}")

            processed = preprocess_image(img)
            text = extract_text(processed, lang_option)

            st.image(img, width=300)
            all_text += f"\n--- Page {i+1} ---\n{text}"

    # ==========================
    # OUTPUT
    # ==========================
    st.subheader("📄 Extracted Text")
    st.write(all_text)

    # Download button
    st.download_button(
        label="⬇️ Download Text",
        data=all_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("🚀 Built with Streamlit + Tesseract OCR")