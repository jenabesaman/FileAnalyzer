import cv2
import numpy as np
import time

# Load both images

# pattern_img = cv2.imread('C:/Workarea/File_Analyser/Aber/ima.JPG')
# second_img = cv2.imread('C:/Workarea/File_Analyser/Aber/pattern.jpg')
#
image = cv2.imread('C:/Workarea/File_Analyser/check/images (9).jpg')

# Resize the image to a consistent size
image = cv2.resize(image, (400, 250))
#
# # Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply Gaussian blur for noise reduction
blurred_image1 = cv2.GaussianBlur(image, (5, 5), 0)
blurred_image2 = cv2.blur(image, (3,2),cv2.BORDER_DEFAULT)
blurred_image3=cv2.bilateralFilter(image,9,10,10)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

cv2.imshow('Edges', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Perform edge detection
edges1 = cv2.Canny(blurred_image1, 50, 150)
edges2 = cv2.Canny(blurred_image2, 50, 150)
edges3 = cv2.Canny(blurred_image3, 50, 150)

cv2.imshow('Edges', edges1)
cv2.imshow('Edges2', edges2)
cv2.imshow('Edges3', edges3)

cv2.waitKey(0)
cv2.destroyAllWindows()



# cv2.imwrite(filename="c:/Workarea/File_Analyser/check/source/" +
#                      "source3.JPG", img=edges2)
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#





# image=cv2.imread("C:/Workarea/File_Analyser/check/download.jpg")
pattern_img = cv2.imread('C:/Workarea/File_Analyser/check/source/Check_pattern2.JPG')
# second_img = cv2.imread(base64_string)
result = cv2.matchTemplate(image, pattern_img, cv2.TM_CCOEFF_NORMED)
threshold = 0.165
locations = np.where(result >= threshold)
if len(locations[0]) > 0:
    print("ok")
