import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

train_dataset = ImageFolder('C:/Workarea/File_Analyser/Pictures', transform=transform)
# val_dataset = ImageFolder('path/to/val_dataset', transform=transform)


import torch
from torch.utils.data import DataLoader

batch_size = 32

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
# val_loader = DataLoader(val_dataset, batch_size=batch_size)

import torchvision.models as models
import torch.nn as nn

model = models.resnet50(pretrained=True)

# Modify the final fully connected layer for your classification task
num_classes = 1
model.fc = nn.Linear(model.fc.in_features, num_classes)

import torch.optim as optim

# Define a loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 10
train_loss, train_acc = 0, 0
for epoch in range(num_epochs):
    model.train()
    for inputs, labels in train_loader:

        outputs = model(inputs)
        loss = criterion(outputs, labels)
        train_loss += loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Validation loop
    model.eval()
    correct = 0
    total = 0
    # with torch.no_grad():
    #     for inputs, labels in val_loader:
    #         outputs = model(inputs)
    #         _, predicted = torch.max(outputs.data, 1)
    #         total += labels.size(0)
    #         correct += (predicted == labels).sum().item()
    print(f'Epoch {epoch + 1}/{num_epochs} {train_loss}')


torch.save(obj=model.state_dict(),f="C:/Workarea/File_Analyser/main/modelscardmelli.pth")

    # print(f'Epoch {epoch + 1}/{num_epochs}, Accuracy: {100 * correct / total:.2f}%')
