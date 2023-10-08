import cv2

# Load the image
image = cv2.imread('C:/Workarea/File_Analyser/check/okcheck.jpg')

# Get the dimensions of the image
x, y, _ = image.shape
print(y)
# Define the coordinates for cropping (e.g., top-left quarter)
x_start = 0
y_start = 0
x_end = x // 2
y_end = y // 5
print(y_end)

# Crop the image based on the specified coordinates
cropped_image = image[y_start:y_end, x_start:x_end]

# Save the cropped image to a new file
cv2.imwrite('cropped_image.jpg', cropped_image)
