import base64
import imghdr

from pyzbar.pyzbar import decode
import numpy as np
import torch
import cv2
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def predicting(base64_string: str):
    def is_base64_image(base64_string=base64_string):
        try:
            image_bytes = base64.b64decode(base64_string)

            # image_format = imghdr.what(None, image_bytes)

            image_array = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            if image is not None:
                return True, image
            else:
                return False, None
        except Exception as e:
            return False, None

    is_image, image = is_base64_image(base64_string)

    if is_image:
        def Decode_QRCode():
            # image = cv2.imread(is_base64_image(base64_string).image)
            for threshold_value in range(0, 256, 10):
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
                decoded_objects = decode(thresholded_image)
                if len(decoded_objects) == 1:
                    for obj in decoded_objects:
                        if len(obj.data.decode('utf-8')) == 75:
                            return True

        def Detect_CreditCard():
            pattern_img = cv2.imread('source.JPG')
            # second_img = cv2.imread(base64_string)
            result = cv2.matchTemplate(image, pattern_img, cv2.TM_CCOEFF_NORMED)
            threshold = 0.21
            locations = np.where(result >= threshold)
            if len(locations[0]) > 0:
                return True

        def Detect_Faces():
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            # image = cv2.imread(base64_string)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
            if len(faces) == 1:
                for (x, y, w, h) in faces:
                    if image.shape[0] - w < int(2.2 * w) and image.shape[1] - h < int(2 * h):
                        return True

        def Detect_MelliCard():
            device = "cuda" if torch.cuda.is_available() else "cpu"
            transform = transforms.Compose([transforms.Resize((224, 320)),
                                            transforms.Grayscale(num_output_channels=3), transforms.ToTensor(),
                                            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                                 std=[0.229, 0.224, 0.225])])
            model = models.resnet18(weights='ResNet18_Weights.DEFAULT')
            num_features = model.fc.in_features
            model.fc = nn.Linear(num_features, 1)
            model = model.to(device)
            model.load_state_dict(torch.load("model11.pth", map_location='cpu'))


            def predict_image(image):
                # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                image = transform(Image.fromarray(image)).unsqueeze(0)
                image = image.to(device)
                with torch.no_grad():
                    output = model(image)
                prob = torch.sigmoid(output)
                return prob.item()

            prediction = predict_image(image)
            if prediction > 0.94:
                return True

        if Decode_QRCode():
            return 1
        elif Detect_CreditCard():
            return 2
        elif Detect_Faces():
            return 3
        elif Detect_MelliCard():
            return 4
        else:
            return 5
    else:
        return "The input is not a valid base64 image."
