# Face Detection System

Ứng dụng nhận dạng khuôn mặt sử dụng OpenCV và Haar Cascade Classifier, chạy được cho ảnh tĩnh và webcam.

## 📋 Mục lục

- [Giới thiệu](#giới-thiệu)
- [Tính năng](#tính-năng)
- [Yêu cầu](#yêu-cầu)
- [Cài đặt](#cài-đặt)
- [Chạy nhanh](#chạy-nhanh)
- [Sử dụng](#sử-dụng)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Kiểm thử](#kiểm-thử)
- [Xử lý sự cố](#xử-lý-sự-cố)
- [Thiết kế hệ thống](#thiết-kế-hệ-thống)

## Giới thiệu

Face Detection System là ứng dụng Python nhận dạng khuôn mặt từ ảnh tĩnh và webcam bằng Haar Cascade. Ứng dụng này cho phép:

- Phát hiện khuôn mặt trong ảnh tĩnh
- Phát hiện khuôn mặt real-time từ webcam
- Vẽ khung nhận dạng và hiển thị FPS
- Lưu kết quả ảnh và video
- Ghi log hoạt động và xử lý lỗi

## Tính năng

- 📷 Phát hiện khuôn mặt từ ảnh tĩnh
- 🎥 Phát hiện khuôn mặt từ webcam
- 🔲 Vẽ khung quanh khuôn mặt
- 📊 Hiển thị số khuôn mặt và FPS
- 💾 Lưu ảnh/video đã xử lý
- ⌨️ Phím tắt điều khiển nhanh trong webcam mode
- 🛡️ Xử lý lỗi và báo log chi tiết

## Yêu cầu

- Python 3.7 trở lên
- OpenCV
- NumPy

## Cài đặt

### 1. Cài dependencies

```bash
cd d:\Zeroace_detection_project
pip install -r requirements.txt
```

### 2. Tải file Haar Cascade

File `haarcascade_frontalface_default.xml` phải nằm trong thư mục dự án.

- Cách đơn giản nhất:

```bash
python setup.py
```

- Hoặc dùng script:

```bash
python download_cascade.py
```

- Nếu cần tải thủ công, lấy từ:

https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

### 3. Kiểm tra cài đặt

```bash
python -c "import cv2; print(cv2.__version__)"
python -c "import numpy; print(numpy.__version__)"
```

## Chạy nhanh

```bash
python setup.py
python main.py
```

## Sử dụng

### Mode 1: Ảnh tĩnh

1. Chọn `1` từ menu
2. Nhập đường dẫn ảnh hoặc để trống để chọn từ thư mục `images/`
3. Ứng dụng sẽ load ảnh, phát hiện khuôn mặt và vẽ khung
4. Chọn có lưu ảnh không

### Mode 2: Webcam

1. Chọn `2` từ menu
2. Webcam sẽ mở và xử lý real-time
3. Phím tắt:
   - `Q` hoặc `ESC`: Thoát
   - `S`: Lưu frame
   - `V`: Bắt đầu/dừng ghi video
   - `P`: Tạm dừng/tiếp tục

## Cấu trúc dự án

```
face_detection_project/
├── main.py
├── config.py
├── detector.py
├── image_processor.py
├── camera.py
├── utils.py
├── setup.py
├── download_cascade.py
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── README.md
├── .gitignore
├── images/
├── output/
└── logs/
```

## Kiểm thử

### Chạy test tự động với pytest

```bash
pip install -r requirements.txt
pytest -q
```

### Test thủ công

- Chạy `python main.py`
- Chọn `1` để kiểm thử ảnh tĩnh
- Chọn `2` để kiểm thử webcam
- Kiểm tra thư mục `output/` để xem ảnh/video đã lưu

## Xử lý sự cố

### `ModuleNotFoundError: No module named 'cv2'`

```bash
pip install opencv-python
```

### `haarcascade_frontalface_default.xml not found`

```bash
python setup.py
```

### Webcam không mở được

- Kiểm tra webcam đã kết nối và không bị ứng dụng khác chiếm dụng
- Thử đóng Zoom/Teams
- Khởi động lại chương trình

## Thiết kế hệ thống

Ứng dụng có cấu trúc OOP chính:

- `Application`: điều khiển menu và các mode
- `FaceDetector`: phát hiện khuôn mặt và vẽ kết quả
- `ImageProcessor`: tải, resize, convert ảnh
- `CameraManager`: điều khiển webcam, capture và ghi video
- `utils`: hàm tiện ích, logging và validation

### Mô tả nhanh các lớp

- `FaceDetector`: sử dụng Haar Cascade để detect faces, apply NMS và trả về danh sách boxes
- `ImageProcessor`: load ảnh, chuyển sang grayscale, resize và lưu ảnh
- `CameraManager`: mở camera, capture frame, ghi video và nhận thông tin camera

## Ghi chú

Tài liệu đã được hợp nhất vào `README.md`. Các file Markdown phụ khác đã được loại bỏ để giữ tài liệu chung và dễ quản lý.
