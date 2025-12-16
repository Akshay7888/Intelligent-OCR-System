# Intelligent-OCR-System
# Intelligent OCR & Document Understanding System

## Overview
This project implements an AI-powered OCR system to extract structured information from scanned documents, PDFs, and DOCX files.

## Features
- OCR for images (PNG, JPG)
- Intelligent PDF handling (text-based + scanned)
- DOCX text extraction
- OCR accuracy improvement with preprocessing
- Regex-based entity extraction
- Flask web interface

## Tech Stack
- Python
- Tesseract OCR
- OpenCV
- pdfplumber
- Flask

## How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
