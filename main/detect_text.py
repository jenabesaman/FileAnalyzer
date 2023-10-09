import cv2
from pytesseract import pytesseract
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract

image = cv2.imread('C:/Workarea/File_Analyser/Text/photo_2023-10-09_11-10-13.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred=cv2.blur(gray,(3,2),cv2.BORDER_DEFAULT)
text = pytesseract.image_to_string(blurred)


print("Detected Text:")
print(text)
print("-" * 50)


threshold_levels = range(40,170,10)
for threshold_level in threshold_levels:
    _, thresholded = cv2.threshold(gray, threshold_level, 255, cv2.THRESH_BINARY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.blur(thresholded, (3,2),cv2.BORDER_DEFAULT)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    cv2.imshow("text", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Use Tesseract to extract text from the processed image
    text = pytesseract.image_to_string(edges)

    print(f"Threshold: {threshold_level}")
    print("Detected Text:")
    print(text)
    print("-" * 50)

# Save or display the final result as needed
cv2.imwrite('output.jpg', edges)