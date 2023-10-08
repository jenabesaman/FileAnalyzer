import cv2


def detect_faces(image_path):
    # Load the Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input image
    image = cv2.imread(image_path)
    print(f"shape: {image.shape}")

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    print(f"len faces {len(faces)}")
    output_text = f"Detected Faces: {len(faces)}\n"
    if len(faces) > 0:
        print(f"Found {len(faces)} face(s) in the image.")
        for (x, y, w, h) in faces:
            print(x,y,w,h)
            # Draw rectangles around detected faces
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Save or display the image with detected faces
        cv2.imwrite("output.jpg", image)
        for i, (x, y, w, h) in enumerate(faces, start=1):
            output_text += f"Face {i} - X: {x}, Y: {y}, Width: {w}, Height: {h}\n"
        print(output_text)
        print(image.shape[0]-w<int(2.2*w),image.shape[1]- h <int(1.5*h))
        if image.shape[0]-w<int(1.5*w) and image.shape[1]- h <int(1.5*h):
            print("personal")
    else:
        print("No faces found in the image.")



if __name__ == "__main__":
    input_image = "C:/Workarea/File_Analyser/face/hamedi.jpg"  # Replace with your input image path
    detect_faces(input_image)
