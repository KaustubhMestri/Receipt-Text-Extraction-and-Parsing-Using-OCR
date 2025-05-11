Receipt Text Extraction and Parsing Using OCR
This Python project uses pytesseract to extract text from images (like receipts) and parse key information, such as:

Date

Amount

Store Name

The extracted data is then displayed or saved for further processing.

🛠️ Requirements
Python 3.x

pytesseract: Python wrapper for Tesseract-OCR

Pillow: Python Imaging Library (PIL)

re: For regular expressions

Install Dependencies
You can install the necessary Python libraries using pip:

bash
Copy
Edit
pip install pytesseract pillow
Tesseract Installation
To run this project, you need to have Tesseract OCR installed on your machine. Follow the installation instructions for your OS.

For Windows, after installation, update the tesseract_cmd in the code to the path where Tesseract is installed. For example:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
🚀 Usage
Replace the image_path variable with the path to the image file you want to process.

Run the Python script to extract text from the image and parse it for key details like date, amount, and store name.

Example
python
Copy
Edit
image_path = r'path_to_your_receipt_image.jpg'
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
Sample Output:
markdown
Copy
Edit
------ Extracted Text ------
Date: 12/05/2025
Rs. 123.50
Store: SuperMart
----------------------------
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

Additional Sections (Optional):
Contributing:
Add guidelines if you want others to contribute to your project.

Acknowledgments:
Mention any third-party resources, libraries, or inspirations.
