import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r'D:\Aaryan_Documents\2.jpg'
img = Image.open(image_path)

text = pytesseract.image_to_string(img)

print("------ Extracted Text ------")
print(text)
print("----------------------------")

date = re.search(r'\d{2}/\d{2}/\d{4}', text)
amount = re.search(r'Rs\.?\s?\d+\.?\d*', text)
store = re.search(r'(?:Store|Shop|Market):?\s?(.*)', text, re.IGNORECASE)

print("Date:", date.group() if date else "Not found")
print("Amount:", amount.group() if amount else "Not found")
print("Store:", store.group(1) if store else "Not found")