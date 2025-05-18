import cv2  # To work with images
import pytesseract  # To read text from images
import json  # To show results nicely

# Tell Python where Tesseract is (it reads text)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def load_image(image_path):
    """Load the image and make it clear."""
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Can't find image at", image_path)
        return None
    # Make it black and white (grayscale)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Make text stand out
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh


def get_text(image):
    """Read text from the image."""
    if image is None:
        return ""
    try:
        # Show Tesseract version
        print("Tesseract version:", pytesseract.get_tesseract_version())
        # Read text from image
        text = pytesseract.image_to_string(image)
        print("Text from image:")
        print(text)
        return text
    except:
        print("Error: Tesseract failed. Check if it's at 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'")
        return ""


def find_details(text):
    """Find store name, total amount, and items."""
    details = {
        "store_name": "",
        "total_amount": "",
        "items": []
    }

    # Break text into lines
    lines = text.split("\n")

    # Find store name (look for store names or a good line)
    for line in lines:
        line = line.lower().strip()
        # Check for common stores or companies
        if line and any(store in line for store in ["walmart", "ucb", "target", "amazon", "costco"]):
            details["store_name"] = line.title()
            break
        # Pick a line that's not a header (longer than 3 chars, not a page number)
        if line and len(line) > 3 and "page" not in line and not details["store_name"]:
            details["store_name"] = line.title()

    # Find total amount (USD like $X.XX or EUR like X.XXX,XX)
    for line in lines:
        line = line.lower()
        # Look for lines with total, amount, paid, or due
        if any(word in line for word in ["total", "amount", "paid", "due"]):
            for word in line.split():
                # Check for $X.XX or X.XXX,XX or X,XXX.XX
                if word.startswith("$") or ("," in word and word.replace(",", "").replace(".", "").isdigit()):
                    details["total_amount"] = word
                    break
            if details["total_amount"]:
                break

    # Find items (lines that look like products)
    for line in lines:
        line = line.lower().strip()
        # Skip empty lines or lines with total/amount/paid/due
        if not line or any(word in line for word in ["total", "amount", "paid", "due"]):
            continue
        # Skip lines that are just numbers or have special characters
        if line.replace(".", "").replace(",", "").isdigit() or any(c in line for c in "@%*"):
            continue
        # Add lines that seem like products (longer than 5 chars)
        if len(line) > 5:
            details["items"].append(line)

    return details


def main():
    """Run the program to read the bill."""
    # Path to the image
    image_path = r"C:\Users\kaust\Desktop\1.jpg"

    # Load the image
    image = load_image(image_path)
    if image is None:
        return

    # Get the text
    text = get_text(image)

    # Find the details
    details = find_details(text)

    # Show the results
    print("\nBill Details:")
    print(json.dumps(details, indent=2))


if __name__ == "__main__":
    main()