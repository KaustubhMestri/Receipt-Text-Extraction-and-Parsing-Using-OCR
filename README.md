# Receipt Text Extraction and Parsing Using OCR

This Python project uses **pytesseract** to extract text from images (like receipts) and parse key information, such as:

- **Date**
- **Amount**
- **Store Name**

The extracted data is then displayed or saved for further processing.

## 🛠️ Requirements

- Python 3.x
- **pytesseract**: Python wrapper for Tesseract-OCR
- **Pillow**: Python Imaging Library (PIL)
- **re**: For regular expressions

### Install Dependencies

You can install the necessary Python libraries using `pip`:

```bash
pip install pytesseract pillow
