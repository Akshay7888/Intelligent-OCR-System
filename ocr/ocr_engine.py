import cv2
import pytesseract
from pdf2image import convert_from_path
from docx import Document
import os
import pdfplumber

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -------- Level 3: Tesseract tuning --------
TESSERACT_CONFIG = r"-l eng --oem 3 --psm 6"


# -------- Level 4: Post-OCR cleanup --------
def clean_ocr_text(text):
    replacements = {
        "Al": "AI",
        "dntamship": "Internship",
        "BRL": "LAB",
        "0CR": "OCR",
        "Ml": "ML"
    }

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    return text


def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    # ---------------- IMAGE FILES ----------------
    if ext in [".png", ".jpg", ".jpeg"]:
        img = cv2.imread(file_path)
        if img is None:
            raise ValueError("Image could not be read")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
        gray = cv2.medianBlur(gray, 3)

        text = pytesseract.image_to_string(gray, config=TESSERACT_CONFIG)
        text = clean_ocr_text(text)

    # ---------------- PDF FILES ----------------
    elif ext == ".pdf":
        text = ""

        # 1️⃣ Try text-based extraction first
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # 2️⃣ Fallback to OCR if text-based extraction fails
        if len(text.strip()) < 50:
            pages = convert_from_path(
                file_path,
                poppler_path=r"C:\poppler\Library\bin",
                dpi=300
            )
            for page in pages:
                page_text = pytesseract.image_to_string(
                    page,
                    config=TESSERACT_CONFIG
                )
                page_text = clean_ocr_text(page_text)
                text += page_text

    # ---------------- DOCX FILES ----------------
    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        raise ValueError("Unsupported file format")

    return text
