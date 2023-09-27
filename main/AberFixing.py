import cv2
import numpy as np

def if_CreditCard(file_path:str):
    pattern_img = cv2.imread('C:/Workarea/File_Analyser/Aber/source.JPG')
    second_img = cv2.imread(file_path)
    # second_img = cv2.imread('C:/Workarea/File_Analyser/Aber/2.jpg')
    pattern_img = cv2.resize(pattern_img, (100, 50))
    image = cv2.resize(second_img, (400, 250))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 50, 150)
    result = cv2.matchTemplate(second_img, pattern_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.2
    locations = np.where(result >= threshold)
    # Check if any matches were found
    if len(locations[0]) > 0:
        print("Pattern exists in the second image.")
    else:
        print("Pattern does not exist in the second image.")

if_CreditCard(file_path="C:/Workarea/File_Analyser/Aber/2.jpg")