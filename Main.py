import cv2
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Can't find image at", image_path)
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return thresh


def get_text(image):
    if image is None:
        return ""
    try:
        print("Tesseract version:", pytesseract.get_tesseract_version())
        text = pytesseract.image_to_string(image)
        print("Text from image:")
        print(text)
        return text
    except:
        print("Error: Tesseract failed. Check if it's at 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'")
        return ""


def find_details(text):
    details = {
        "store_name": "",
        "total_amount": "",
        "items": []
    }

    lines = text.split("\n")

    for line in lines:
        line = line.lower().strip()
        if line and any(store in line for store in ["walmart", "ucb", "target", "amazon", "costco"]):
            details["store_name"] = line.title()
            break
        if line and len(line) > 3 and "page" not in line and not details["store_name"]:
            details["store_name"] = line.title()

    for line in lines:
        line = line.lower()
        if any(word in line for word in ["total", "amount", "paid", "due"]):
            for word in line.split():
                if word.startswith("$") or ("," in word and word.replace(",", "").replace(".", "").isdigit()):
                    details["total_amount"] = word
                    break
            if details["total_amount"]:
                break

    for line in lines:
        line = line.lower().strip()
        if not line or any(word in line for word in ["total", "amount", "paid", "due"]):
            continue
        if line.replace(".", "").replace(",", "").isdigit() or any(c in line for c in "@%*"):
            continue
        if len(line) > 5:
            details["items"].append(line)

    return details


def main():
    image_path = r"C:\Users\kaust\Desktop\1.jpg"
    image = load_image(image_path)
    if image is None:
        return
    text = get_text(image)
    details = find_details(text)
    print("\nBill Details:")
    print(json.dumps(details, indent=2))


if __name__ == "__main__":
    main()
