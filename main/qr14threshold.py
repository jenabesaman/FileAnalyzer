import cv2
from pyzbar.pyzbar import decode
image = cv2.imread('C:/Workarea/File_Analyser/check/okcheck.jpg')

# x, y, _ = image.shape
#
# print(y)
# # Define the coordinates for cropping (e.g., top-left quarter)
# x_start = 0
# y_start =0
# x_end = x//3
# y_end = int(y//3)
is_qr=False
for threshold_value in range(0, 256, 10):  # Change the step size and range as needed
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Decode QR codes using Pyzbar
    decoded_objects = decode(thresholded_image)


    # Print the threshold value and detected QR codes
    print(f"Threshold Value: {threshold_value}")


    for obj in decoded_objects:
        print(f"test: {decoded_objects}")
        print(f"Data: {obj.data.decode('utf-8')}, len: {len(obj.data.decode('utf-8'))}")
        if len(obj.data.decode('utf-8'))==75:
            is_qr=True


    # Display the image with detected QR codes (optional)
    cv2.imshow(f"Threshold {threshold_value}", thresholded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print(is_qr )
