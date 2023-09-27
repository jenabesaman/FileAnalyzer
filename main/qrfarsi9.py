import cv2
from pyzbar.pyzbar import decode

# تابعی برای تشخیص و خواندن کدهای QR از تصویر
def read_qr_code(image_path):
    # خواندن تصویر با استفاده از OpenCV
    image = cv2.imread(image_path)

    # تبدیل تصویر به مقیاس خاکستری (Grayscale)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # تشخیص و خواندن کدهای QR
    decoded_objects = decode(gray)

    # نمایش محتوای کدهای QR
    for obj in decoded_objects:
        print("نوع: ", obj.type)
        print("محتوا: ", obj.data.decode('utf-8'))

# تست تابع با یک تصویر چک صیادی
image_path = 'C:/Workarea/File_Analyser/check/okcheck.jpg'  # جایگزین کنید با مسیر تصویر واقعی شما
read_qr_code(image_path)
