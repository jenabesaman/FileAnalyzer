import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image

# Load the pre-trained ResNet-18 model
resnet_model = models.resnet18(pretrained=True)

# Freeze all layers to keep the pre-trained weights
for param in resnet_model.parameters():
    param.requires_grad = False

# Replace the final classification layer for binary classification
num_features = resnet_model.fc.in_features
resnet_model.fc = nn.Linear(num_features, 1)

def classify_image(image_path, model, threshold=0.5):
    # Load and preprocess the image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)

    # Put the model in evaluation mode
    model.eval()

    # Forward pass
    with torch.no_grad():
        output = torch.sigmoid(model(image))

    # Check if the output probability is above the threshold
    is_car = output.item() > threshold

    return is_car

image_path = 'path_to_your_image.jpg'  # Replace with the path to your image
is_car = classify_image(image_path, resnet_model)

if is_car:
    print("The input picture contains a car.")
else:
    print("The input picture does not contain a car.")


#i want a one class cllasification problem with torch with resnet model.

