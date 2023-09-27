import cv2
from pyzbar.pyzbar import decode
import os
def DecodeQRCode(file_path: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    else:
        is_qr = False
        image = cv2.imread(file_path)
        for threshold_value in range(0, 256, 10):
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
            decoded_objects = decode(thresholded_image)
            if len(decoded_objects) == 1:
                for obj in decoded_objects:
                    print(f"len:{len(obj.data.decode('utf-8'))}")
                    if len(obj.data.decode('utf-8')) == 75:
                        is_qr = True
                        return is_qr
            elif threshold_value == 250:
                return is_qr

print(DecodeQRCode(file_path='C:/Workarea/File_Analyser/check/dasmal.jpg'))
