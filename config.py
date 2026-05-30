# -*- coding: utf-8 -*-
"""
Module cấu hình (config.py)
====================================
Định nghĩa toàn bộ hằng số, đường dẫn, tham số cấu hình cho ứng dụng nhận dạng khuôn mặt.

Chức năng:
- Đường dẫn file cascade
- Tham số nhận dạng
- Cấu hình hiển thị
- Đường dẫn input/output
- Cài đặt logging

Tác giả: Trần Thành Nam
Phiên bản: 1.0
"""

import os
from pathlib import Path

# ========== THÔNG TIN ỨNG DỤNG ==========
APP_NAME = "Face Detection System"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Trần Thành Nam"

# ========== ĐƯỜNG DẪN ==========
# Thư mục gốc dự án
BASE_DIR = Path(__file__).resolve().parent

# Đường dẫn file Haar Cascade
CASCADE_PATH = str(BASE_DIR / "haarcascade_frontalface_default.xml")

# Đường dẫn thư mục input/output
IMAGES_DIR = str(BASE_DIR / "images")
OUTPUT_DIR = str(BASE_DIR / "output")
LOGS_DIR = str(BASE_DIR / "logs")

# Tạo thư mục nếu không tồn tại
for directory in [IMAGES_DIR, OUTPUT_DIR, LOGS_DIR]:
    os.makedirs(directory, exist_ok=True)

# ========== THAM SỐ NHẬN DẠNG KHUÔN MẶT ==========
# Scale factor - kích thước giảm ở mỗi lần lặp (1.05-1.3)
SCALE_FACTOR = 1.1

# Minimum neighbors - số lượng láng giềng tối thiểu để giữ lại khuôn mặt (4-6)
MIN_NEIGHBORS = 5

# Kích thước tối thiểu của khuôn mặt (pixel)
MIN_FACE_SIZE = (30, 30)

# Kích thước tối đa của khuôn mặt
MAX_FACE_SIZE = (500, 500)

# ========== THAM SỐ VẼ ==========
# Màu vẽ khung (BGR format cho OpenCV)
FACE_COLOR = (0, 255, 0)  # Xanh lục

# Màu text (BGR)
TEXT_COLOR = (255, 0, 0)  # Xanh dương

# Độ dày đường vẽ
RECTANGLE_THICKNESS = 2

# Độ dày text
TEXT_THICKNESS = 1

# Font chữ
FONT = "cv2.FONT_HERSHEY_SIMPLEX"

# Kích thước font
FONT_SCALE = 0.6

# ========== THAM SỐ WEBCAM ==========
# ID camera (0 = camera mặc định)
CAMERA_ID = 0

# Chiều rộng frame
FRAME_WIDTH = 640

# Chiều cao frame
FRAME_HEIGHT = 480

# FPS mong muốn
TARGET_FPS = 30

# Codec video (MJPEG - tương thích tốt)
VIDEO_CODEC = "MJPG"

# ========== THAM SỐ XỬ LÝ ==========
# Resize ảnh để tăng tốc độ xử lý
RESIZE_SCALE = 0.5  # Resize xuống 50%

# Độ sáng tối thiểu để xử lý
MIN_BRIGHTNESS = 50

# ========== THAM SỐ LƯỚI CẮT (NMS - Non-Maximum Suppression) ==========
# Ngưỡng IOU để coi hai box là overlap
IOU_THRESHOLD = 0.3

# ========== THAM SỐ LOGGING ==========
# Mức logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = "INFO"

# Format log
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# File log
LOG_FILE = os.path.join(LOGS_DIR, "face_detection.log")

# ========== PHÍM TẮT ĐIỀU KHIỂN ==========
KEY_QUIT = ord('q')          # Thoát
KEY_SAVE = ord('s')          # Lưu ảnh/frame
KEY_PAUSE = ord('p')         # Tạm dừng
KEY_BRIGHTNESS_UP = ord('+')  # Tăng độ sáng
KEY_BRIGHTNESS_DOWN = ord('-') # Giảm độ sáng

# ========== THÔNG BÁO LỖI ==========
ERROR_CASCADE_NOT_FOUND = "Lỗi: File Haar Cascade không tìm thấy tại {}"
ERROR_IMAGE_NOT_FOUND = "Lỗi: Ảnh không tìm thấy tại {}"
ERROR_CAMERA_NOT_OPENED = "Lỗi: Không thể mở webcam"
ERROR_INVALID_INPUT = "Lỗi: Đầu vào không hợp lệ"

# ========== THÔNG ĐIỆP THÀNH CÔNG ==========
MSG_IMAGE_SAVED = "✓ Ảnh đã lưu: {}"
MSG_FACE_DETECTED = "✓ Phát hiện {} khuôn mặt"
MSG_NO_FACE = "✗ Không phát hiện khuôn mặt"

# ========== CẤu HÌNH NÂNG CAO ==========
# Cho phép hiển thị FPS
SHOW_FPS = True

# Cho phép hiển thị thông tin chi tiết
SHOW_DETAILS = True

# Số frame lấy trung bình FPS
FPS_AVERAGE_FRAMES = 30

# ========== THƯ VIỆN ĐƯỢC SỬ DỤNG ==========
REQUIRED_LIBRARIES = [
    "opencv-python>=4.5.0",
    "numpy>=1.20.0"
]

if __name__ == "__main__":
    print(f"✓ {APP_NAME} v{APP_VERSION}")
    print(f"Base directory: {BASE_DIR}")
    print(f"Cascade path: {CASCADE_PATH}")
    print(f"Images directory: {IMAGES_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Logs directory: {LOGS_DIR}")
    print(f"\n✓ Cấu hình hoàn tất!")
