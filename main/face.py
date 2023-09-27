from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN
from PIL import Image

# Load an image
image = Image.open('C:/Workarea/File_Analyser/etc/not_melli/download1.jpg')

# Convert the image to RGB (if it's in a different format)
image = image.convert('RGB')

# Convert the image to a numpy array
pixels = plt.imread(image)

# Initialize the MTCNN detector
detector = MTCNN()

# Detect faces in the image
faces = detector.detect_faces(pixels)

# Display the image with bounding boxes around the detected faces
plt.imshow(pixels)

# Check if only one face is detected
if len(faces) == 1:
    print("Image contains exactly one face.")
else:
    print("Image does not contain exactly one face or no faces detected.")

# Draw bounding boxes around detected faces
for face in faces:
    x, y, width, height = face['box']
    rect = Rectangle((x, y), width, height, fill=False, color='red')
    plt.gca().add_patch(rect)

plt.axis('off')
plt.show()
