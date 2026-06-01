# CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ

## 2.1. Giới thiệu hệ thống

### "Hệ thống nhận dạng khuôn mặt sử dụng OpenCV"

"Hệ thống Nhận Dạng Khuôn Mặt" là một ứng dụng hiện đại dùng để phát hiện và xác định vị trí các khuôn mặt trong ảnh tĩnh hoặc video từ webcam. Hệ thống sử dụng thuật toán Haar Cascade Classifier của OpenCV - một phương pháp học máy mạnh mẽ trong việc nhận dạng đặc trưng hình ảnh.

#### a) Mục tiêu chính

Người dùng có thể:
- Phát hiện khuôn mặt từ các ảnh tĩnh được chọn
- Phát hiện khuôn mặt real-time từ webcam
- Lưu ảnh/video kết quả với các khuôn mặt được đánh dấu
- Theo dõi thống kê (FPS, số lượng khuôn mặt)
- Điều khiển các chế độ xử lý một cách dễ dàng qua menu

#### b) Menu chính

Gồm **3 chế độ chính**:

```
┌─ MENU CHÍNH ──────────────────────────────┐
│                                           │
│  [1] Phát hiện khuôn mặt từ ảnh tĩnh     │
│  [2] Phát hiện khuôn mặt từ webcam       │
│  [0] Thoát chương trình                  │
│                                           │
└───────────────────────────────────────────┘
```

- **Chế độ 1 (Ảnh tĩnh):** Người dùng chọn ảnh từ thư mục `images/`, hệ thống phát hiện khuôn mặt và hiển thị kết quả
- **Chế độ 2 (Webcam):** Kích hoạt webcam, xử lý real-time, hỗ trợ ghi video
- **Chế độ 0 (Thoát):** Đóng ứng dụng một cách an toàn

#### c) Cách sử dụng

**Mode Ảnh Tĩnh:**
- Chọn ảnh từ thư mục hoặc nhập đường dẫn
- Hệ thống sẽ phát hiện tất cả khuôn mặt trong ảnh
- Hiển thị ảnh kết quả với khung nhận diện
- Tùy chọn lưu ảnh

**Mode Webcam (Phím tắt):**
- `Q`: Thoát chương trình
- `S`: Lưu frame hiện tại
- `V`: Bắt đầu/dừng ghi video
- `P`: Tạm dừng/tiếp tục xử lý
- `ESC`: Thoát nhanh

#### d) Thông tin hiển thị

- **FPS (Frames Per Second):** Số khung hình xử lý mỗi giây
- **Số lượng khuôn mặt:** Tổng số khuôn mặt phát hiện được
- **Kích thước khuôn mặt:** Độ rộng × độ cao (pixels) của từng khuôn mặt
- **Trạng thái ghi video:** Hiển thị "REC" khi đang ghi video

#### e) Kết quả và lưu trữ

- Ảnh kết quả được lưu trong thư mục `output/`
- Video được lưu dưới dạng `.avi` với codec MJPG
- Log chi tiết được ghi trong `logs/face_detection.log`
- Tên file tự động tạo với timestamp (VD: `output_2025-06-01_143022.png`)

---

## 2.2. Phân tích hệ thống

### Kiến trúc tổng thể

Hệ thống được thiết kế theo **mô hình lập trình hướng đối tượng (OOP)** với các thành phần độc lập, dễ bảo trì và mở rộng.

```
┌─────────────────────────────────────────────────────────────┐
│                   ỨNG DỤNG CHÍNH (main.py)                 │
│                  (Application Manager)                      │
└────────────┬────────────────────────────┬──────────────────┘
             │                            │
      ┌──────▼──────┐         ┌──────────▼────────┐
      │              │         │                   │
      │   detector.py │      │   camera.py        │
      │ (FaceDetector)│      │(CameraManager)     │
      │              │       │                    │
      └──────┬──────┘         └────────┬──────────┘
             │                         │
      ┌──────▼──────┐         ┌──────────▼────────┐
      │              │         │                   │
      │ config.py    │      │image_processor.py│
      │(Cấu hình)    │      │ (ImageProcessor)   │
      │              │       │                    │
      └──────────────┘       └────────────────────┘
             ▲                          ▲
             │                          │
             └──────────────┬───────────┘
                            │
                      ┌─────▼─────┐
                      │ utils.py   │
                      │ (Utilities)│
                      └────────────┘
```

### Các file chính

| File | Chức năng | Vai trò |
|------|----------|--------|
| `main.py` | Điểm vào chính, quản lý menu, xử lý mode ảnh/webcam | Controller chính |
| `detector.py` | Phát hiện khuôn mặt sử dụng Haar Cascade, vẽ khuôn mặt | Xử lý nhận dạng |
| `camera.py` | Quản lý webcam, capture frame, ghi video | Xử lý input từ camera |
| `image_processor.py` | Xử lý ảnh, resize, enhance | Tiền xử lý ảnh |
| `config.py` | Định nghĩa tất cả hằng số, tham số, đường dẫn | Cấu hình hệ thống |
| `utils.py` | Các hàm tiện ích: logging, I/O, tính toán | Hỗ trợ chung |

### Thư mục dự án

```
Tran_Thanh_Nam-Th30.03/
├── main.py                              # Ứng dụng chính
├── detector.py                          # Module nhận dạng
├── camera.py                            # Module camera
├── image_processor.py                   # Module xử lý ảnh
├── config.py                            # Cấu hình
├── utils.py                             # Tiện ích
├── haarcascade_frontalface_default.xml  # Mô hình Haar Cascade
├── images/                              # Thư mục ảnh đầu vào
├── output/                              # Thư mục lưu kết quả
├── logs/                                # Thư mục lưu log
├── tests/                               # Thư mục test
├── requirements.txt                     # Dependency
└── README.md                            # Tài liệu
```

---

## 2.3. Thiết kế hệ thống

### Mô hình lớp (Class Diagram)

#### 1. Lớp `FaceDetector` (detector.py)

**Mô tả:** Lớp chính để phát hiện và xử lý khuôn mặt sử dụng Haar Cascade Classifier.

**Thuộc tính:**
- `face_cascade` (cv2.CascadeClassifier): Mô hình Haar Cascade đã load
- `scale_factor` (float): Hệ số giảm kích thước ở mỗi lần lặp (1.1 mặc định)
- `min_neighbors` (int): Số lượng láng giềng tối thiểu để xác nhận khuôn mặt (5 mặc định)
- `min_size` (Tuple): Kích thước tối thiểu của khuôn mặt (30×30 pixels)
- `max_size` (Tuple): Kích thước tối đa của khuôn mặt (500×500 pixels)
- `last_faces` (List): Danh sách khuôn mặt từ lần phát hiện gần nhất
- `detection_time` (float): Thời gian phát hiện (milliseconds)

**Phương thức chính:**
- `__init__()`: Khởi tạo detector, load cascade file
- `detect_faces(image, apply_nms)`: Phát hiện khuôn mặt trong ảnh
  - Convert ảnh sang grayscale
  - Gọi `detectMultiScale()` từ cascade
  - Áp dụng NMS (Non-Maximum Suppression) để loại bỏ overlap
  - Return danh sách (x, y, width, height)
  
- `apply_nms(faces, iou_threshold)`: Loại bỏ các khuôn mặt overlap
  - Tính IoU (Intersection over Union) giữa các box
  - Giữ lại những box có IoU < threshold
  
- `draw_faces(image, faces)`: Vẽ khung nhận diện lên ảnh
  - Vẽ hình chữ nhật xung quanh từng khuôn mặt
  - Ghi số thứ tự và kích thước
  - Hiển thị tổng số khuôn mặt
  
- `get_face_count()`: Trả về số lượng khuôn mặt
- `get_largest_face()`: Trả về khuôn mặt lớn nhất
- `get_detection_stats()`: Trả về thống kê chi tiết

---

#### 2. Lớp `CameraManager` (camera.py)

**Mô tả:** Quản lý webcam, capture frame, ghi video.

**Thuộc tính:**
- `camera` (cv2.VideoCapture): Đối tượng capture từ webcam
- `frame_width` (int): Chiều rộng frame (640 pixels)
- `frame_height` (int): Chiều cao frame (480 pixels)
- `fps` (int): Tốc độ khung hình (30 FPS)
- `video_writer` (cv2.VideoWriter): Đối tượng ghi video
- `frame_count` (int): Số frame đã capture
- `recording` (bool): Trạng thái ghi video

**Phương thức chính:**
- `open_camera()`: Mở webcam, thiết lập độ phân giải
- `capture_frame()`: Lấy frame từ webcam
- `close_camera()`: Đóng webcam an toàn
- `start_video_recording(output_path)`: Bắt đầu ghi video
- `stop_video_recording()`: Dừng ghi video
- `write_frame_to_video(frame)`: Ghi frame vào file video
- `get_frame_count()`: Lấy số frame đã capture
- `print_properties()`: In các thông số camera

---

#### 3. Lớp `ImageProcessor` (image_processor.py)

**Mô tả:** Xử lý ảnh - load, resize, enhance.

**Thuộc tính:**
- `original_image` (np.ndarray): Ảnh gốc
- `processed_image` (np.ndarray): Ảnh sau xử lý
- `image_size` (Tuple): Kích thước ảnh (width, height)

**Phương thức chính:**
- `load_image(image_path)`: Load ảnh từ đường dẫn
- `get_original_image()`: Lấy ảnh gốc
- `get_processed_image()`: Lấy ảnh sau xử lý
- `resize_image(scale)`: Resize ảnh (giảm độ phân giải để tăng tốc độ)
- `enhance_brightness(delta)`: Tăng/giảm độ sáng
- `enhance_contrast(alpha)`: Tăng/giảm độ tương phản
- `convert_grayscale()`: Convert sang grayscale

---

#### 4. Lớp `Application` (main.py)

**Mô tả:** Lớp ứng dụng chính, quản lý flow và các module.

**Thuộc tính:**
- `detector` (FaceDetector): Bộ phát hiện khuôn mặt
- `image_processor` (ImageProcessor): Bộ xử lý ảnh
- `camera` (CameraManager): Bộ quản lý camera
- `fps_counter` (FPSCounter): Bộ đếm FPS

**Phương thức chính:**
- `__init__()`: Khởi tạo tất cả module
- `show_menu()`: Hiển thị menu chính
- `select_image_path()`: Chọn ảnh từ thư mục
- `run_image_mode()`: Xử lý mode ảnh tĩnh
- `run_camera_mode()`: Xử lý mode webcam real-time
- `run()`: Vòng lặp chính, xử lý lựa chọn menu

---

### Quy trình xử lý

#### Flowchart tổng quát

```
┌─────────────────┐
│  Start App      │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│  Show Main Menu     │
└────────┬────────────┘
         │
    ┌────┴────┬─────────┬─────────┐
    │          │         │         │
    ▼          ▼         ▼         ▼
┌─────────┐ ┌────────┐ ┌──────┐ ┌────────┐
│Mode 1   │ │Mode 2  │ │Mode 0│ │Invalid │
│(Image)  │ │(Camera)│ │(Exit)│ │Choice  │
└────┬────┘ └────┬───┘ └──┬───┘ └──┬─────┘
     │            │        │        │
     ▼            ▼        ▼        ▼
┌──────────┐  ┌─────────┐ │  ┌───────────┐
│Select    │  │Open     │ │  │Show Error │
│Image     │  │Camera   │ │  │Message    │
└────┬─────┘  └────┬────┘ │  └─────┬─────┘
     │             │      │        │
     ▼             ▼      │        │
┌──────────┐  ┌──────────┐│        │
│Load      │  │While Cam │         │
│Image     │  │Is Open:  │         │
└────┬─────┘  │ -Capture │         │
     │        │  Frame   │         │
     ▼        │ -Detect  │         │
┌──────────┐  │  Face    │         │
│Detect    │  │ -Draw &  │         │
│Face      │  │  Show    │         │
└────┬─────┘  └────┬─────┘         │
     │             │                │
     ▼             ▼                │
┌──────────┐  ┌──────────┐         │
│Draw Face │  │Handle    │         │
│On Image  │  │Keys: Q,S │         │
└────┬─────┘  │V,P,ESC   │         │
     │        └────┬─────┘         │
     ▼             │                │
┌──────────┐      │                │
│Save      │      ▼                │
│Result    │  ┌──────────┐         │
└────┬─────┘  │Cleanup   │         │
     │        │Camera    │         │
     └────┬───┴────┬─────┴─────┬───┘
          │        │           │
          └────┬───┴───────────┘
               │
               ▼
         ┌──────────────┐
         │Back to Menu? │
         └──┬───────┬──┐
            │       │  │
       Yes  │       │  No
            │       │  │
            └───┬───┘  └──► Exit
                │
                ▼
           ┌──────────┐
           │Show Menu │
           └──────────┘
```

#### Quy trình Mode Ảnh Tĩnh

```
1. Chọn Menu [1]
   ↓
2. Nhập đường dẫn ảnh hoặc chọn từ danh sách
   ↓
3. Load ảnh bằng ImageProcessor.load_image()
   ↓
4. Detector.detect_faces(image)
   ├─ Convert BGR → Grayscale
   ├─ Cascade.detectMultiScale()
   ├─ Apply NMS
   └─ Sort by size
   ↓
5. Detector.draw_faces(image, faces)
   ├─ Draw rectangles
   ├─ Add labels
   └─ Show info
   ↓
6. Hiển thị ảnh kết quả
   ↓
7. Lưu ảnh? (Y/N)
   ├─ Y → utils.save_image() → output/
   └─ N → Tiếp tục
   ↓
8. Quay lại Menu
```

#### Quy trình Mode Webcam

```
1. Chọn Menu [2]
   ↓
2. Camera.open_camera()
   ├─ Khởi tạo cv2.VideoCapture
   └─ Set độ phân giải (640×480)
   ↓
3. While Camera.is_open():
   │
   ├─ Camera.capture_frame()
   │  │
   │  ├─ Read frame từ camera
   │  └─ Return frame
   │
   ├─ Detector.detect_faces(frame)
   │  │
   │  ├─ Phát hiện khuôn mặt
   │  └─ Return list faces
   │
   ├─ Detector.draw_faces(frame, faces)
   │
   ├─ Calculate & Draw FPS
   │
   ├─ cv2.imshow() Display frame
   │
   ├─ cv2.waitKey(1) & 0xFF
   │  │
   │  ├─ Q/ESC → Break loop
   │  ├─ S → Save frame
   │  ├─ V → Toggle video recording
   │  └─ P → Pause/Resume
   │
   └─ If recording: Write frame to video
   ↓
4. Cleanup & Close Camera
   ↓
5. Quay lại Menu
```

---

### Mô hình dữ liệu

#### Định dạng dữ liệu khuôn mặt

Một khuôn mặt được biểu diễn dưới dạng **tuple** `(x, y, w, h)`:
- `x` (int): Tọa độ X góc trái trên
- `y` (int): Tọa độ Y góc trái trên
- `w` (int): Chiều rộng (width)
- `h` (int): Chiều cao (height)

```python
face = (100, 50, 80, 100)  # x=100, y=50, width=80, height=100
# Tính tọa độ góc phải dưới:
x2 = x + w = 180
y2 = y + h = 150
```

#### Định dạng log

```
2025-06-01 14:30:22,123 - root - INFO - Khởi động Face Detection System v1.0
2025-06-01 14:30:22,456 - root - INFO - Khởi tạo ứng dụng...
2025-06-01 14:30:22,789 - detector - DEBUG - ✓ Load cascade từ: haarcascade_frontalface_default.xml
2025-06-01 14:30:25,234 - main - INFO - Phát hiện 3 khuôn mặt
```

#### Định dạng tệp đầu ra

**Ảnh:**
```
output_2025-06-01_143022.png
format: output_YYYY-MM-DD_HHMMSS.png
```

**Video:**
```
video_2025-06-01_143022.avi
format: video_YYYY-MM-DD_HHMMSS.avi
codec: MJPG
```

---

### Thuật toán Haar Cascade

#### Nguyên lý hoạt động

**Haar Cascade** là một cascade classifier dùng nhiều tầng (stages) để phát hiện đặc trưng:

```
Stage 1: Features cơ bản (độ tương phản, cạnh)
   ↓
Stage 2: Kết hợp features cấp 1
   ↓
Stage 3: Kết hợp features cấp 2
   ↓
...
   ↓
Stage N: Quyết định cuối cùng
   ↓
Output: Danh sách khuôn mặt phát hiện được
```

**Tham số chính:**
- `scaleFactor = 1.1`: Hình ảnh được giảm kích thước 1.1x ở mỗi lần lặp
- `minNeighbors = 5`: Cần ít nhất 5 láng giềng xác nhận một phát hiện
- `minSize = (30, 30)`: Khuôn mặt nhỏ hơn 30×30 bị bỏ qua
- `maxSize = (500, 500)`: Khuôn mặt lớn hơn 500×500 bị bỏ qua

#### Non-Maximum Suppression (NMS)

NMS loại bỏ các bounding box overlap:

```
Bước 1: Sắp xếp theo diện tích (lớn → bé)
Bước 2: Chọn box lớn nhất, giữ lại
Bước 3: Tính IoU với tất cả box còn lại
Bước 4: Bỏ những box có IoU > threshold (0.3)
Bước 5: Lặp lại cho box tiếp theo
```

**IoU (Intersection over Union):**
```
IoU = Diện tích giao / Diện tích hợp
    = (Overlap Area) / (Area A + Area B - Overlap Area)
```

---

### Công nghệ sử dụng

| Thành phần | Công nghệ | Phiên bản |
|-----------|-----------|----------|
| Thư viện chính | OpenCV | ≥4.5.0 |
| Tính toán | NumPy | ≥1.20.0 |
| Ngôn ngữ | Python | ≥3.7 |
| Logging | Built-in logging | Chuẩn Python |
| Video I/O | OpenCV VideoCapture | Built-in |

---

## 2.4. Tính năng mở rộng

Hệ thống được thiết kế để dễ dàng mở rộng:

1. **Thêm nhận dạng mắt/miệng:**
   - Load cascade khác
   - Thêm EyeDetector, MouthDetector class

2. **Thêm tracking:**
   - Sử dụng centroid tracking
   - Gán ID cho từng khuôn mặt

3. **Deep Learning:**
   - Thay Haar Cascade bằng YOLO, SSD, hoặc RetinaFace
   - Tích hợp TensorFlow/PyTorch

4. **Database:**
   - Lưu thông tin khuôn mặt
   - So khớp với cơ sở dữ liệu

5. **Streaming:**
   - Hỗ trợ RTSP stream
   - Phát hiện từ nhiều camera

---

## 2.5. Xử lý lỗi

Hệ thống có cơ chế xử lý lỗi toàn diện:

```python
# Kiểm tra cascade file
if not utils.is_valid_cascade(cascade_path):
    raise ValueError(f"Cascade file không hợp lệ: {cascade_path}")

# Kiểm tra ảnh input
if image is None or image.size == 0:
    logger.warning("Ảnh đầu vào trống")
    return []

# Xử lý webcam
try:
    frame = self.camera.capture_frame()
except Exception as e:
    logger.error(f"Lỗi capture frame: {e}")
    return False
```

---

## 2.6. Yêu cầu hiệu năng

| Thành phần | Yêu cầu |
|-----------|--------|
| CPU | Dual-core, 2.0 GHz+ |
| RAM | 2 GB |
| Lưu trữ | 500 MB (code + models) |
| Webcam | 30 FPS, 640×480 |
| FPS hiện tại | ~25-30 FPS (640×480) |
| Độ trễ | <100ms (từ capture đến display) |

---

**Tác giả:** Trần Thành Nam  
**Phiên bản:** 1.0  
**Cập nhật:** 2025-06-01
