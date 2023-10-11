import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH ="C:/Workarea/File_Analyser/melli/20230917195815973.jpg"

custom_characters = {'0': '٠', '5': '٥'}
image = cv2.imread(IMAGE_PATH)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred_image2 = cv2.blur(gray_image, (3,2),cv2.BORDER_DEFAULT)
# edges1 = cv2.Canny(blurred_image2, 50, 150)
reader = easyocr.Reader(lang_list=['fa'])
result = reader.readtext(image,paragraph="False")
print(result)