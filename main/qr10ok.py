import cv2
import numpy as np
from pyzbar import pyzbar

image = cv2.imread("C:/Workarea/File_Analyser/check/test2.jpg")
# image = cv2.resize(image, (640, 850))

red = (0, 0, 255)
blue = (255, 0, 0)
qrcode_color = (255, 255, 0)
barcode_color = (0, 255, 0)

# decode and detect the QR codes and barcodes
barcodes = pyzbar.decode(image)

# initialize the total number of QR codes and barcodes
qr_code = 0
code = 0

for barcode in barcodes:
    # extract the points of th polygon of the barcode and create a Numpy array
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1,1,2))

    # check to see if this is a QR code or a barcode
    if barcode.type == "QRCODE":
        qr_code += 1
        cv2.polylines(image, [pts], True, qrcode_color, 3)
    elif barcode.type == "CODE128":
        code += 1
        cv2.polylines(image, [pts], True, barcode_color, 3)

    # decode the barcode data and draw it on the image
    text = "{}".format(barcode.data.decode("utf-8"))
    cv2.putText(image, text, (barcode.rect[0] + 10, barcode.rect[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, red, 2)
    print(text)

# Display the number of QR codes and barcodes detected
if len(barcodes) == 0:
    text = "No barcode found on this image"
    cv2.putText(image, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, blue, 2)
else:
    text = "{} QR code(s) found on this image".format(qr_code)
    cv2.putText(image, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, blue, 2)
    text = "{} barcode(s) found on this image".format(code)
    cv2.putText(image, text, (20, 43), cv2.FONT_HERSHEY_SIMPLEX, 0.75, blue, 2)

cv2.imshow("Image", image)
cv2.waitKey(0)

