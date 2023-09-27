import cv2
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image
import matplotlib.pyplot as plt

device = "cpu"


# class OneClassDataset(torch.utils.data.Dataset):
#     def __init__(self, data_dir, transform=None):
#         self.data_dir = data_dir
#         self.transform = transform
#         self.image_files = os.listdir(data_dir)
#
#     def __len__(self):
#         return len(self.image_files)
#
#     def __getitem__(self, idx):
#         img_name = os.path.join(self.data_dir, self.image_files[idx])
#         image = Image.open(img_name)
#
#         if self.transform:
#             image = self.transform(image)
#
#         return image


class CustomDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.image_files = os.listdir(data_dir)
        # self.image_paths = []  # List of image file paths

    #     # Populate image_paths with the paths to your dataset images
    #
    # def __len__(self):
    #     return len(self.image_paths)

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_name = os.path.join(self.data_dir, self.image_files[idx])
        # image = Image.open(img_name)

        image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)  # Read image in grayscale

        # Apply thresholding using cv2.threshold
        _, thresholded_image = cv2.threshold(image, 136, 255, cv2.THRESH_BINARY)

        if self.transform:
            # image = self.transform(thresholded_image)
            image = self.transform(Image.fromarray(thresholded_image))

        return image

    # def __getitem__(self, idx):
    #     # img_path = self.image_paths[idx]
    #     image = cv2.imread(data_dir, cv2.IMREAD_GRAYSCALE)  # Read image in grayscale
    #
    #     # Apply thresholding using cv2.threshold
    #     _, thresholded_image = cv2.threshold(image, 136, 255, cv2.THRESH_BINARY)
    #
    #     if self.transform:
    #         thresholded_image = self.transform(thresholded_image)
    #
    #     return thresholded_image


transform = transforms.Compose([
    transforms.Resize((224, 320)),
    transforms.Grayscale(num_output_channels=3),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# img_path = ("C:/Workarea/File_Analyser/etc/not_melli/download.jpg")
# image = Image.open("C:/Workarea/File_Analyser/etc/not_melli/download.jpg")
# image=CustomDataset("C:/Workarea/File_Analyser/etc/not_melli/download.jpg")


# image = cv2.imread(img_path)  # Read image in grayscale
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# _, thresholded_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
# image = transform(thresholded_image)
# plt.imshow(thresholded_image,cmap='gray')
# plt.axis(False)
# plt.show()

# image = transform(img_path)
# image=image.squeeze(0).permute(1,2,0)
# plt.imshow(image)
# plt.axis(False)
# plt.show()


data_dir = 'C:/Workarea/File_Analyser/melli_total/dataset/melli'
dataset = CustomDataset(data_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

model = models.resnet18(pretrained=True)
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 1)
model = model.to(device)  # Move the model to GPU if available
model.load_state_dict(torch.load("C:/Workarea/File_Analyser/main/models/model8.pth", map_location='cpu'))
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.00005)

num_epochs = 15
for epoch in range(num_epochs):
    for inputs in dataloader:
        model.train()
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, torch.ones_like(outputs))  # Target label is 1 (positive)
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch + 1}/{num_epochs}] Loss: {loss.item():.4f}')

torch.save(obj=model.state_dict(), f="C:/Workarea/File_Analyser/main/models/model9.pth")


# model.load_state_dict(torch.load("C:/Workarea/File_Analyser/main/models/model8.pth", map_location='cpu'))
def predict_image(image_path):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)
    image = image.to(device)

    with torch.no_grad():
        output = model(image)

    prob = torch.sigmoid(output)

    return prob.item()


new_image_path = 'C:/Workarea/File_Analyser/etc/not_melli/img_625.jpg'
prediction = predict_image(new_image_path)
print(prediction)

if prediction > 0.94:
    print("The image belongs to the class.")
else:
    print("The image does not belong to the class.")
