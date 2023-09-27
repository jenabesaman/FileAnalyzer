import torch
import cv2
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import os

def prediction(file_path: str):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    transform = transforms.Compose([
        transforms.Resize((224, 320)), transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    model = models.resnet18(weights='ResNet18_Weights.DEFAULT')
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, 1)
    model = model.to(device)
    model.load_state_dict(torch.load("C:/Workarea/File_Analyser/main/models/model11.pth", map_location='cpu'))
    def predict_image(image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = transform(Image.fromarray(image)).unsqueeze(0)
        image = image.to(device)
        with torch.no_grad():
            output = model(image)
        prob = torch.sigmoid(output)
        return prob.item()
    prediction = predict_image(file_path)
    print(prediction)
    if prediction > 0.94:
        print("The image belongs to the class.")
    else:
        print("The image does not belong to the class.")

prediction(file_path='C:/Workarea/File_Analyser/etc/not_melli/saman.jpg')
