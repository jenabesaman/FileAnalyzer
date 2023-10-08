import cv2
from pyzbar.pyzbar import decode

def recognize_qr_code(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Decode QR codes in the image
    decoded_objects = decode(gray_image)

    # Extract QR code texts
    qr_code_texts = []
    for obj in decoded_objects:
        qr_code_texts.append(obj.data.decode('utf-8'))

    return qr_code_texts

if __name__ == "__main__":
    image_path = "C:/Workarea/File_Analyser/check/okcheck.jpg"  # Replace with the path to your image
    qr_code_texts = recognize_qr_code(image_path)

    if qr_code_texts:
        print("QR Code(s) found:")
        for i, qr_code_text in enumerate(qr_code_texts, start=1):
            print(f"QR Code {i}: {qr_code_text}")
    else:
        print("No QR Codes found in the image.")
