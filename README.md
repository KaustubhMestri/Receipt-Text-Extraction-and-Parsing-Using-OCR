# Receipt Analyzer

## 📁 Project Structure

```
receipt-analyzer/
├── main.py                 # Main script for processing receipts
├── Data/                   # Folder to store test receipt images
├── README.md               # Project documentation
```

## 📌 Project Overview

The **Receipt Analyzer** is a Python-based system designed to extract and analyze structured data from receipt images using Optical Character Recognition (OCR) and simple Natural Language Processing (NLP) techniques.

This project simulates real-world applications like budgeting tools or expense tracking apps, offering practical experience in combining image processing and text analysis.

## ✅ Objectives

* Extract text from a receipt image (e.g., grocery, retail, or restaurant receipts).
* Use OCR (Tesseract) and basic image processing (OpenCV) for text extraction.
* Use simple NLP techniques to:

  * Identify the store name
  * Extract the date and total amount
  * Classify purchased items into categories (e.g., food, household)

## 💡 Example Output

Given a receipt image, the system might return:

```json
{
  "store": "Walmart",
  "date": "2025-04-20",
  "total": "$15.47",
  "categories": {
    "food": ["milk", "bread"],
    "household": ["detergent"]
  }
}
```

## 🔧 Tools and Technologies

* **Python**
* **OpenCV** – Image preprocessing (grayscale conversion, thresholding)
* **Tesseract OCR** (via `pytesseract`) – For text extraction
* **Regex / NLP** – For structured information extraction

## 🛠 Features

* Preprocessing of input receipt images
* Extraction of:

  * Store name
  * Total amount
  * Purchased items
* Item categorization using basic keyword matching
* Printable and structured output in JSON format

## 📂 Input Requirements

* Receipt image in JPG/PNG format (placed in the `Data/` folder)
* Ensure no sensitive or personal information is included in the images

## 🚀 How to Run

1. Install dependencies:

   ```bash
   pip install opencv-python pytesseract
   ```
2. Update the `tesseract_cmd` path in `main.py`:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
3. Run the script:

   ```bash
   python main.py
   ```

## 📋 Deliverables

* ✅ Python script
* ✅ README documentation
* ✅ Sample test images
* ✅ Short report on approach and challenges (not included here)

---
