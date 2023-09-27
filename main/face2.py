import cv2

def is_face_image(image_path):
    # Load the Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if faces were detected
    if len(faces) > 0:
        return True
    else:
        return False

# Test the function with an image file path
image_path = 'C:/Workarea/File_Analyser/etc/not_melli/download.jpg'
is_face = is_face_image(image_path)

if is_face:
    print("The image contains a face.")
else:
    print("The image does not contain a face.")
