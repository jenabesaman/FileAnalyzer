import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH ="C:/Workarea/File_Analyser/melli/20230917195815973.jpg"
image = cv2.imread(IMAGE_PATH)
reader = easyocr.Reader(['fa'])
result = reader.readtext(IMAGE_PATH,paragraph="False")
print(result)
