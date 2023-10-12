import base64
from pyzbar.pyzbar import decode
import numpy as np
import torch
import cv2
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image


class Detection:
    def __init__(self, base64_string: str):
        self.base64_string = base64_string
        self.check_condition = 0
        self.melli_condition = 0
        self.image = None
        self.is_image = None
        self.is_check = 0
        self.is_credit = 0
        self.is_face = 0
        self.is_melli = 0
        self.predicted_enum = None

    def is_base64_image(self):
        try:
            image_bytes = base64.b64decode(self.base64_string)
            image_array = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            if image is not None:
                self.is_image = True
                self.image = image
            else:
                self.is_image = False
                self.image = None
            return self.is_image, self.image
        except Exception as e:
            return False, e

    def Detect_check(self, image):

        def detect_feature():
            pattern_img = cv2.imread('Check_pattern.JPG')
            result = cv2.matchTemplate(image, pattern_img, cv2.TM_CCOEFF_NORMED)
            threshold = 0.2902
            locations = np.where(result >= threshold)
            if len(locations[0]) > 0:
                self.check_condition += 1
                return self.check_condition

        def detect_feature2():
            pattern_img2 = cv2.imread('Check_pattern2.JPG')
            result = cv2.matchTemplate(image, pattern_img2, cv2.TM_CCOEFF_NORMED)
            threshold = 0.20244
            locations = np.where(result >= threshold)
            if len(locations[0]) > 0:
                self.check_condition += 1
                return self.check_condition

        def detect_QR():
            for threshold_value in range(0, 256, 10):
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
                decoded_objects = decode(thresholded_image)
                if len(decoded_objects) == 1:
                    for obj in decoded_objects:
                        if len(obj.data.decode('utf-8')) == 75:
                            self.check_condition += 1
                            return self.check_condition

        detect_feature(), detect_feature2(), detect_QR()
        if self.check_condition >= 2:
            self.is_check = 1
            return self.is_check

    def Detect_CreditCard(self, image):
        pattern_img = cv2.imread('Credit_pattern.jpg')
        # second_img = cv2.imread(base64_string)
        result = cv2.matchTemplate(image, pattern_img, cv2.TM_CCOEFF_NORMED)
        threshold = 0.21
        locations = np.where(result >= threshold)
        if len(locations[0]) > 0:
            self.is_credit = 1
        return self.is_credit

    def Detect_Faces(self, image):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # image = cv2.imread(base64_string)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        if len(faces) == 1:
            for (x, y, w, h) in faces:
                if image.shape[0] - w < int(2.2 * w) and image.shape[1] - h < int(2 * h):
                    self.is_face = 1
                    return self.is_face

    def Detect_MelliCard(self, image):
        # device = "cuda" if torch.cuda.is_available() else "cpu"
        device = "cpu"
        transform = transforms.Compose([transforms.Resize((224, 320)),
                                        transforms.Grayscale(num_output_channels=3), transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                             std=[0.229, 0.224, 0.225])])
        model = models.resnet18(weights='ResNet18_Weights.DEFAULT')
        num_features = model.fc.in_features
        model.fc = nn.Linear(num_features, 1)
        model = model.to(device)
        model.load_state_dict(torch.load("model11.pth", map_location='cpu'))

        def detect_feature():
            pattern_img = cv2.imread('Iran_pattern.JPG')
            result = cv2.matchTemplate(image, pattern_img, cv2.TM_CCOEFF_NORMED)
            threshold = 0.2
            locations = np.where(result >= threshold)
            if len(locations[0]) > 0:
                self.melli_condition += 1
                return self.melli_condition

        def predict_image():
            image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            image = transform(Image.fromarray(image)).unsqueeze(0)
            image = image.to(device)
            with torch.no_grad():
                output = model(image)
            prob = torch.sigmoid(output)
            predict_score = prob.item()
            if predict_score > 0.94:
                self.melli_condition += 1
                return self.melli_condition

        detect_feature(), predict_image()
        if self.melli_condition >= 2:
            self.is_melli = 1
            return self.is_melli

    def handeling(self):
        self.is_image, self.image = self.is_base64_image()
        self.Detect_check(image=self.image)
        self.Detect_CreditCard(image=self.image)
        self.Detect_Faces(image=self.image)
        self.Detect_MelliCard(image=self.image)
        if self.is_image == True:
            # if self.is_check == 1 and self.is_melli_not_check != -1 and self.is_face_not_check != -1 and self.is_credit_not_check != -1:
            if self.is_check == 1 :
                self.predicted_enum = 1
            elif self.is_credit == 1:
                self.predicted_enum = 2
            elif self.is_face == 1:
                self.predicted_enum = 3
            elif self.is_melli == 1:
                self.predicted_enum = 4
            else:
                self.predicted_enum = 5
        else:
            self.predicted_enum = "The input is not a valid base64 image."

        return self.predicted_enum
