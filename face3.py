import cv2
import numpy as np

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the input image
input_image_path = 'C:/Workarea/File_Analyser/face/mehran.jpg'  # Change this to your input image path
output_image_path = 'output.jpg'  # Change this to your desired output image path

# Read the input image
image = cv2.imread(input_image_path)

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces and the whole image
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle around the detected face
cv2.rectangle(image, (0, 0), (image.shape[1], image.shape[0]), (0, 0, 255), 2)  # Draw a red rectangle around the whole image

# Write the coordinates of the detected face(s) and the whole image
output_text = f"Detected Faces: {len(faces)}\n"
for i, (x, y, w, h) in enumerate(faces, start=1):
    output_text += f"Face {i} - X: {x}, Y: {y}, Width: {w}, Height: {h}\n"

print(output_text)

# Put the text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, output_text, (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Save the output image
cv2.imwrite(output_image_path, image)

# Display the output image (optional)
cv2.imshow('Output Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
