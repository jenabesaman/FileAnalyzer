import cv2
import numpy as np
from pyzbar import pyzbar


# Load the image
image = cv2.imread('C:/Workarea/File_Analyser/check/okcheck.jpg')


# Get the dimensions of the image
x, y, _ = image.shape

print(y)
# Define the coordinates for cropping (e.g., top-left quarter)
x_start = 0
y_start =0
x_end = x//3
y_end = int(y//3)
print(y_end)

# Crop the image based on the specified coordinates
cropped_image = image[y_start:y_end, x_start:x_end]

# Save the cropped image to a new file
# cv2.imwrite('C:/Workarea/File_Analyser/check/fixed.jpg', cropped_image)
#
# image = cv2.imread("C:/Workarea/File_Analyser/check/fixed.jpg")



image=cropped_image
scale = 2
width = int(image.shape[1] * scale)
height = int(image.shape[0] * scale)
image = cv2.resize(image, (width, height))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 300, 1000, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# cv2.imshow("img",thresh)

image=thresh

bboxes = []
for cnt in image:
    area = cv2.contourArea(cnt)
    xmin, ymin, width, height = cv2.boundingRect(cnt)
    extent = area / (width * height)

    # filter non-rectangular objects and small objects
    if (extent > np.pi / 4) and (area > 100):
        bboxes.append((xmin, ymin, xmin + width, ymin + height))



# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(gray, 150, 200000, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# kernel = np.ones((3, 3), np.uint8)
# thresh = cv2.dilate(thresh, kernel, iterations=1)
# contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# image=contours

# image=thresh

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

