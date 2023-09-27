import cv2
from pyzbar.pyzbar import decode

# Load an image containing QR codes
image = cv2.imread('C:/Workarea/File_Analyser/check/333.jpg')

# Define a range of thresholds to test
thresholds = [100, 150, 200]

for threshold in thresholds:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the threshold
    _, thresholded_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

    # Decode QR codes from the thresholded image
    decoded_objects = decode(thresholded_image)

    print(f"Threshold: {threshold}")

    for obj in decoded_objects:
        print(f"Data: {obj.data.decode('utf-8')}")
        print(f"Type: {obj.type}")
        print(f"Polygon: {obj.polygon}")

    print("=" * 40)

# You can also adjust the scale factor
scale_factors = [1.0, 1.5, 2.0]

for scale_factor in scale_factors:
    # Resize the image
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

    # Decode QR codes from the scaled image
    decoded_objects = decode(scaled_image)

    print(f"Scale Factor: {scale_factor}")

    for obj in decoded_objects:
        print(f"Data: {obj.data.decode('utf-8')}")
        print(f"Type: {obj.type}")
        print(f"Polygon: {obj.polygon}")

    print("=" * 40)