import cv2
import os
import numpy as np


# Function to extract features from an image
def extract_features(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use a feature extraction method (e.g., SIFT, ORB, etc.)
    # You can choose a different feature extraction method based on your requirements
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray_image, None)

    return descriptors


# Function to compare two images using their feature vectors
def compare_images(image1_features, image2_features):
    # Use a distance metric (e.g., Euclidean distance) to compare feature vectors
    distance = np.linalg.norm(image1_features - image2_features)

    return distance


# Folder containing the images to learn from
learning_folder = 'learning_images/'

# Image to check for in other images
image1_path = 'image1.jpg'

# Extract features from image1
image1_features = extract_features(image1_path)

# Iterate through the images in the learning folder
for filename in os.listdir(learning_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(learning_folder, filename)

        # Extract features from the current image in the folder
        current_image_features = extract_features(image_path)

        # Compare the current image features with image1 features
        distance = compare_images(image1_features, current_image_features)

        # Define a threshold for similarity (you can adjust this threshold)
        similarity_threshold = 100.0

        if distance < similarity_threshold:
            print(f"{image1_path} is similar to {image_path}")
