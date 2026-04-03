# 🧠 Multilingual OCR App

A powerful and user-friendly **OCR (Optical Character Recognition)** web application that extracts text from images and PDFs using **Tesseract OCR** and **Streamlit**.

This app supports **multiple Indian languages**, making it useful for document digitization, note extraction, and multilingual text recognition.

---

## 🚀 Live Demo

🌍 https://multilingual-ocr-app.streamlit.app/

---

## ✨ Features

* 📷 **Image to Text Extraction**
* 📄 **PDF to Text (Multi-page support)**
* 🌐 **Multilingual OCR**

  * English
  * Hindi
  * Bengali
  * Tamil
  * Telugu
  * Marathi
  * Gujarati
  * Kannada
  * Malayalam
  * Punjabi
  * Urdu
  * Sanskrit & more
* ⚙️ **Image Preprocessing**

  * Grayscale conversion
  * Noise removal
  * Thresholding
* 🧠 **Improved OCR Accuracy**
* ⬇️ **Download Extracted Text**
* 🎯 Clean and interactive UI (Streamlit)

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Tesseract OCR**
* **OpenCV**
* **PyMuPDF (fitz)**
* **Pillow (PIL)**
* **NumPy**

---

## 📂 Project Structure

multilingual-ocr-app/
│── app.py              # Main Streamlit app
│── requirements.txt    # Python dependencies
│── packages.txt        # System dependencies (Tesseract)
│── README.md           # Project documentation

---

## ⚙️ Installation & Setup (Local)

### 🔹 1. Clone Repository

git clone https://github.com/Mandeepkumarsaw/multilingual-ocr-app.git
cd multilingual-ocr-app

---

### 🔹 2. Install Dependencies

pip install -r requirements.txt

---

### 🔹 3. Install Tesseract (Windows)

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

After installation, set path in code:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

---

### 🔹 4. Run App

streamlit run app.py

---

## ☁️ Deployment (Streamlit Cloud)

### Required Files:

#### 📄 requirements.txt

streamlit
pytesseract
pillow
numpy
PyMuPDF
opencv-python-headless

#### 📄 packages.txt

tesseract-ocr
tesseract-ocr-all

---

### Steps:

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Click **New App**
4. Select repo & app.py
5. Click **Deploy**

---

## 📸 Screenshots

(Add screenshots here for better presentation)

---

## 🎯 Use Cases

* 📚 Digitizing handwritten/printed notes
* 🧾 Extracting text from scanned documents
* 📰 Newspaper & book OCR
* 🌐 Multilingual document processing
* 🏫 Student projects & research

---

## ⚠️ Known Limitations

* Handwritten text accuracy may vary
* Low-quality images reduce OCR performance
* Complex layouts may not parse perfectly

---

## 🔮 Future Improvements

* 🔍 Text highlighting in images
* 📊 Export to PDF/Word
* 🧾 Table detection
* 🌙 Dark mode UI
* 🤖 AI-based OCR enhancement

---

## 👨‍💻 Author

**Mandeep Kumar**

---

## ⭐ Support

If you like this project:

* ⭐ Star this repository
* 🍴 Fork it
* 📢 Share with others

---

## 📜 License

This project is open-source and available under the **MIT License**.
