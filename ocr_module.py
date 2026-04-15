import easyocr
import cv2

reader = None

def get_reader():
    global reader
    if reader is None:
        reader = easyocr.Reader(['en'])
    return reader


def process_certificate(image_path):
    reader = get_reader()

    results = reader.readtext(image_path)

    extracted_text = " ".join([res[1] for res in results])

    return {
        "extracted_data": extracted_text,
        "verified": False,
        "tampering_score": 0,
        "final_score": 50,
        "status": "Demo Mode",
        "remarks": "OCR working",
        "ela_image": image_path
    }