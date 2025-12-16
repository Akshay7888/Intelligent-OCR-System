# Intelligent-OCR-System
Intelligent OCR & Document Understanding System:

Overview:
This project implements an Intelligent OCR & Document Understanding System capable of extracting readable text and structured information from multiple document formats. The system is designed to handle real-world documents, including scanned files, digital PDFs, and office documents, and present the extracted content through a simple web interface.

It automatically adapts its extraction strategy based on the document type, ensuring optimal accuracy while maintaining robustness.

Supported File Types:
The system supports the following document formats:
>PDF (text-based and scanned)
>DOCX
>JPG / JPEG
>PNG
Each format is processed using the most suitable extraction technique.


Important:
Security-protected PDFs often block text extraction and OCR by design. This limitation is inherent to document security and not a system defect.


Tech Stack:

>Python
>Flask (Web framework)
>Tesseract OCR
>OpenCV
>pdfplumber
>pdf2image
>python-docx

How to Run the Project
-> python -m venv venv
-> venv\Scripts\activate
-> pip install -r requirements.txt
-> python app.py

Open your browser and navigate to:

http://127.0.0.1:5000


Note:
OCR accuracy varies depending on document quality and security constraints. This project demonstrates a practical and production-oriented approach to document understanding rather than an idealized laboratory setup.
