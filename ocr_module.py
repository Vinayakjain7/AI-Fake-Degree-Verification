import pytesseract
import cv2

# IMPORTANT for Render
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def process_certificate(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return {
        "extracted_data": text,
        "verified": False,
        "tampering_score": 0,
        "final_score": 50,
        "status": "OCR Extracted",
        "remarks": "Using Tesseract OCR",
        "ela_image": image_path
    }