import cv2
import numpy as np
import time
# Load both images

# pattern_img = cv2.imread('C:/Workarea/File_Analyser/Aber/2.JPG' )
# second_img = cv2.imread('C:/Workarea/File_Analyser/Aber/pattern.jpg' )

# image = cv2.imread('C:/Workarea/File_Analyser/melli/20230917195815973.jpg')
#
# # Resize the image to a consistent size
# image = cv2.resize(image, (400, 250))

# Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply Gaussian blur for noise reduction
# blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
# cv2.imshow('Edges', blurred_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # Perform edge detection
# edges = cv2.Canny(blurred_image, 50, 150)
#
# cv2.imwrite(filename="C:/Workarea/File_Analyser/melli/source/"+"source.JPG",img=edges)
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# first_image=cv2.resize(pattern_img,(400,250))
# first_image=cv2.cvtColor(first_image,cv2.COLOR_BGR2GRAY)
# first_image=cv2.GaussianBlur(first_image,(5,5),0)
# first_image=cv2.Canny(first_image,50,150)
# cv2.imshow("show",first_image)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
#
#
# pattern_img=cv2.resize(pattern_img,(100,50))

# image = cv2.resize(second_img, (400, 250))
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply Gaussian blur for noise reduction
# blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
# edges = cv2.Canny(blurred_image, 50, 150)
# cv2.imshow("show",edges)
# cv2.waitKey()
# cv2.destroyAllWindows()

# # Perform template matching
# result = cv2.matchTemplate(second_img, pattern_img, cv2.TM_CCOEFF_NORMED)
# # result = cv2.matchTemplate(edges, pattern_img, cv2.TM_CCOEFF_NORMED)
# cv2.imshow("show",result)
# # cv2.waitKey()
# # cv2.destroyAllWindows()
#
# # Set a threshold (you can adjust this)
# threshold = 0.2
#
# # Find locations where the similarity score is above the threshold
# locations = np.where(result >= threshold)

# Check if any matches were found
# if len(locations[0]) > 0:
#     print("Pattern exists in the second image.")
# else:
#     print("Pattern does not exist in the second image.")
# end=time.time()
#
# print(f"timing: {end-start }")

image=cv2.imread("C:/Workarea/File_Analyser/melli/source/20230917195815843.jpg")
pattern_img = cv2.imread('C:/Workarea/File_Analyser/melli/source/pattern.jpg')
# second_img = cv2.imread(base64_string)
result = cv2.matchTemplate(image, pattern_img, cv2.TM_CCOEFF_NORMED)
threshold = 0.21
locations = np.where(result >= threshold)
if len(locations[0]) > 0:
    print("ok")
