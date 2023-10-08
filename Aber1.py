import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Load the image
image = cv2.imread('C:/Workarea/File_Analyser/Aber/2.jpg')

# Resize the image to a consistent size
image = cv2.resize(image, (400, 250))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur for noise reduction
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
cv2.imshow('Edges', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Perform edge detection
edges = cv2.Canny(blurred_image, 50, 150)
cv2.imwrite(filename="CANDYABER1.JPG",img=edges)

# Extract text using pytesseract (you need to install pytesseract and provide the correct path)
import pytesseract

text = pytesseract.image_to_string(blurred_image)

# Visualize the extracted edges (optional)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print extracted text
print("Extracted Text:")
print(text)
