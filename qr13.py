import cv2
import numpy as np
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from kraken import binarization
from PIL import Image
from qreader import QReader

image_path = r"C:\Users\ASinger\Pictures\hdi_pdfs\page1.png"

# Method 1
im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
ret, bw_im = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
barcodes = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
print(f'barcodes: {barcodes}')

# Method 2
im = Image.open(image_path)
bw_im = binarization.nlbin(im)
decoded = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
print(f'decoded: {decoded}')

# Method 3
im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(im, (5, 5), 0)
ret, bw_im = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
decoded = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
print(f'decoded: {decoded}')

# Method 4
qreader = QReader()
image = cv2.imread(image_path)
decoded_text = qreader.detect_and_decode(image=image)
print(f'decoded_text: {decoded_text}')

# Method 5
cropped_image = image_path
im2 = Image.open(cropped_image)
im2 = im2.resize((2800, 2800))
im2.save(cropped_image, quality=500)
im2.show()
im3 = cv2.imread(cropped_image, cv2.IMREAD_GRAYSCALE)
ret, bw_im = cv2.threshold(im3, 127, 255, cv2.THRESH_BINARY)
decoded = decode(bw_im, symbols=[ZBarSymbol.QRCODE])
print(f'decoded: {decoded}')