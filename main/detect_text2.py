import cv2
import doctr
import numpy as np
from doctr.models import ocr_predictor
from doctr.io import DocumentFile

# Load the image
image = cv2.imread('your_image.jpg')

# Perform text detection
detection_results = ocr_predictor.detect(image)

# Perform text recognition
for result in detection_results:
    recognized_text = ocr_predictor.recognize(image, result)

    # Use or store the recognized_text as needed
    print(recognized_text)



# from doctr.models import recognition_predictor
# predictor = recognition_predictor('crnn_vgg16_bn')
# print(predictor.model.cfg['vocab'])
