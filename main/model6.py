import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import os
from PIL import Image
data_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
data_dir = 'C:/Workarea/File_Analyser'
train_dataset = datasets.ImageFolder(os.path.join(data_dir, 'dataset'), transform=data_transforms)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(64 * 28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        x = self.fc_layers(x)
        return x

model = ConvNet()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 25
for epoch in range(num_epochs):
    for inputs, _ in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, torch.ones_like(outputs))  # Target label is 1 (positive)
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch + 1}/{num_epochs}] Loss: {loss.item():.4f}')
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = data_transforms(image).unsqueeze(0)
    return image

image_path = 'C:/Workarea/File_Analyser/etc/not_melli/download1.jpg'
input_image = preprocess_image(image_path)
with torch.no_grad():
    output = model(input_image)
    if output.item() > 0.9:  # You can adjust the threshold as needed
        print(f"The image belongs to the class.{output.item()}")
    else:
        print(f"The image does not belong to the class.{output.item()}")
