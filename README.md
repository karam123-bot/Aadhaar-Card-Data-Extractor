# Aadhaar Card Data Extractor

This Python script extracts Aadhaar card information (Aadhaar number, Name, and Date of Birth) from image files using Optical Character Recognition (OCR) powered by Tesseract. The extracted information is saved to a CSV file, and the processed images can be saved for reference.

## Features

- Extract Aadhaar card details (Aadhaar number, Name, Date of Birth) from `.jpg`, `.jpeg`, and `.png` images.
- Save the extracted information to a CSV file for easy access and analysis.
- Save the processed images with extracted information for reference.
- Utilizes Tesseract OCR for text extraction from images.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.x
- Tesseract OCR
- Python packages: `pytesseract`, `PIL` (Pillow), `re`, `csv`, `os`

### Installation

1. Install Python packages:

   ```bash
   pip install pytesseract Pillow
