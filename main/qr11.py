import cv2

image = cv2.imread('C:/Workarea/File_Analyser/check/qr.jpg')

qrCodeDetector = cv2.QRCodeDetector()
print(qrCodeDetector)
decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
print(decodedText)
qr_data = decodedText.split(',')
print(qr_data)
# qr_size = qr_data[0]
# top = qr_data[1]
# right = qr_data[2]
# bottom = qr_data[3]
# left = qr_data[4]
#
# print(f'Size: {qr_size}' + str(qr_data[5]))
# print(f'Top: {top}')
# print(f'Right: {right}')
# print(f'Bottom: {bottom}')
# print(f'Left: {left}')
# if points is not None:
#     pts = len(points)
#     print(pts)
#     for i in range(pts):
#         nextPointIndex = (i+1) % pts
#         cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
#         print(points[i][0])
#     print(decodedText)
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("QR code not detected")