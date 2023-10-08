import cv2
import os


def detect_faces(file_path: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    output = False
    if len(faces) == 1:
        for (x, y, w, h) in faces:
            if image.shape[0] - w < int(2.2* w) and image.shape[1] - h < int(2 * h):
                output = True
                return output
            else:
                return output
    else:
        return output


print(detect_faces(file_path="C:/Workarea/File_Analyser/face/hamedi.jpg"))
