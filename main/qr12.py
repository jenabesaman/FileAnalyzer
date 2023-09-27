import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from pyzbar.pyzbar import decode
from PIL import Image
resnet_model = resnet50(pretrained=True)
resnet_model.eval()
def extract_features(image_path, model):
    # Load and preprocess the image
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = preprocess(image).unsqueeze(0)  # Add batch dimension

    # Extract features using ResNet-50
    with torch.no_grad():
        features = model(image)

    return features
image_path = 'C:/Workarea/File_Analyser/check/test.jpg'
image_features = extract_features(image_path, resnet_model)
large_image_path = 'C:/Workarea/File_Analyser/check/okcheck.jpg'
large_image = Image.open(large_image_path)
decoded_qr_codes = decode(large_image)

for qr_code in decoded_qr_codes:
    qr_code_data = qr_code.data.decode('utf-8')
    qr_code_position = qr_code.polygon
    # You can now work with the QR code data and its position in the large image
    print(f"QR Code Data: {qr_code_data}")
    print(f"QR Code Position: {qr_code_position}")
