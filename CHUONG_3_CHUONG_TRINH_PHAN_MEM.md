# CHƯƠNG 3: CHƯƠNG TRÌNH PHẦN MỀM

## 3.1. Giao diện chính (Menu Principal)

### Màn hình khi người dùng mở ứng dụng

```
═══════════════════════════════════════════════════════════════
  Face Detection System v1.0.0
═══════════════════════════════════════════════════════════════

┌─ MENU CHÍNH ──────────────────────────────┐
│                                           │
│  [1] Phát hiện khuôn mặt từ ảnh tĩnh     │
│  [2] Phát hiện khuôn mặt từ webcam       │
│  [0] Thoát chương trình                  │
│                                           │
└───────────────────────────────────────────┘

Chọn lựa chọn (0-2): _
```

**Chức năng từng tùy chọn:**

| Tùy chọn | Chức năng | Mô tả |
|---------|----------|--------|
| **[1]** | **Image Mode** | Phát hiện khuôn mặt từ ảnh tĩnh được chọn |
| **[2]** | **Camera Mode** | Kích hoạt webcam, phát hiện real-time |
| **[0]** | **Quit** | Thoát ứng dụng an toàn |

---

## 3.2. Giao diện Mode Ảnh Tĩnh (Static Image Mode)

### Bước 1: Chọn ảnh

```
┌─ MODE ẢNH TĨNH ────────────────────────────┐
│ Nhập đường dẫn ảnh hoặc để trống để chọn   │
│ từ thư mục 'images'                        │
│ Nhập Q để quay lại menu                    │
└────────────────────────────────────────────┘

1. photo1.jpg
2. photo2.png
3. photo3.bmp

Chọn ảnh (1-3): _
```

**Thao tác:**
- Nhập số (1-3) để chọn ảnh từ danh sách
- Nhập đường dẫn trực tiếp nếu không muốn chọn từ danh sách
- Nhập `Q` để quay lại menu chính

### Bước 2: Xử lý và hiển thị kết quả

```
Đang load ảnh: images/photo1.jpg
✓ Load ảnh thành công

Đang phát hiện khuôn mặt...
✓ Phát hiện: 3 khuôn mặt

Có lưu ảnh không? (y/n): y
✓ Lưu ảnh: output/output_2025-06-01_143022.png

Hiển thị ảnh (Nhấn bất kỳ phím nào để tiếp tục)

┌────────────────────────────────────────────┐
│                                            │
│   [Ảnh khuôn mặt được phát hiện]          │
│   ┌────┐      ┌────┐      ┌────┐         │
│   │Face│      │Face│      │Face│         │
│   │ 1  │      │ 2  │      │ 3  │         │
│   │80x │      │95x │      │70x │         │
│   │100 │      │110 │      │85  │         │
│   └────┘      └────┘      └────┘         │
│                                            │
│  Total: 3 face(s)                         │
│  Detection Time: 45.23 ms                 │
│                                            │
└────────────────────────────────────────────┘

Nhấn Enter để tiếp tục...
```

**Thông tin hiển thị:**
- Tổng số khuôn mặt phát hiện được
- Kích thước từng khuôn mặt (width × height)
- Tọa độ trung tâm (điểm trắng ở giữa)
- Thời gian xử lý (detection time)

### Bước 3: Quay lại Menu

```
Nhấn Enter để tiếp tục...

═══════════════════════════════════════════════════════════════
  Face Detection System v1.0.0
═══════════════════════════════════════════════════════════════

┌─ MENU CHÍNH ──────────────────────────────┐
│                                           │
│  [1] Phát hiện khuôn mặt từ ảnh tĩnh     │
│  [2] Phát hiện khuôn mặt từ webcam       │
│  [0] Thoát chương trình                  │
│                                           │
└───────────────────────────────────────────┘

Chọn lựa chọn (0-2): _
```

---

## 3.3. Giao diện Mode Webcam (Real-time Camera Mode)

### Bước 1: Mở Camera

```
┌─ MODE WEBCAM ──────────────────────────────┐
│ Phím tắt:                                  │
│  Q: Thoát                                  │
│  S: Lưu frame                              │
│  V: Ghi video (bắt đầu/dừng)              │
│  P: Tạm dừng                               │
│ ESC: Thoát                                 │
└────────────────────────────────────────────┘

Đang mở camera...
✓ Camera đã được mở

Camera Properties:
┌─────────────────────────────────┐
│ Frame Width:     640            │
│ Frame Height:    480            │
│ FPS:             30             │
│ Codec:           MJPG           │
└─────────────────────────────────┘

Bắt đầu xử lý... (Nhấn Q để thoát)
```

### Bước 2: Xử lý Real-time

```
┌────────────────────────────────────────────┐
│                                            │
│   [Webcam Feed - Real-time Detection]     │
│   ┌──────────────────────────────────┐    │
│   │                                  │    │
│   │  ●─────────┐                     │    │
│   │  │         │  Face 1             │    │
│   │  │         │  80×100             │    │
│   │  └─────────┘                     │    │
│   │        ●                         │    │
│   │                                  │    │
│   │     ┌──────────┐                 │    │
│   │     │          │  Face 2         │    │
│   │     │    ●     │  95×110         │    │
│   │     │          │                 │    │
│   │     └──────────┘                 │    │
│   │                                  │    │
│   │  Total: 2 face(s)                │    │
│   │  FPS: 28.5 | Faces: 2            │    │
│   └──────────────────────────────────┘    │
│                                            │
│  Detection Time: 35.47 ms                 │
│  Frames Processed: 156                    │
│                                            │
└────────────────────────────────────────────┘
```

**Thông tin real-time:**
- FPS (Frames Per Second): Số khung hình xử lý mỗi giây
- Faces: Số lượng khuôn mặt phát hiện trong frame hiện tại
- Detection Time: Thời gian xử lý 1 frame (milliseconds)
- Frames Processed: Tổng số frame đã xử lý

### Bước 3: Các phím tắt trong Mode Webcam

#### **Q - Thoát chương trình**
```
Nhấn Q:
✓ Thoát chương trình
✓ Xử lý 256 frame
✓ Camera mode hoàn tất

Quay lại Menu...
```

#### **S - Lưu frame hiện tại**
```
Nhấn S:
✓ Frame đã lưu: output/frame_2025-06-01_143045.png

(Tiếp tục xử lý webcam)
```

#### **V - Bắt đầu/dừng ghi video**
```
Nhấn V (lần 1):
✓ Bắt đầu ghi video: output/video_2025-06-01_143050.avi

[Hiển thị "REC" ở góc trên trái]

Nhấn V (lần 2):
✓ Dừng ghi video
✓ Video được lưu (512 frames)

(Tiếp tục xử lý webcam)
```

#### **P - Tạm dừng/tiếp tục**
```
Nhấn P (lần 1):
✓ Tạm dừng

[Frame hiện tại được giữ nguyên, không cập nhật]

Nhấn P (lần 2):
✓ Tiếp tục

[Webcam tiếp tục xử lý]
```

#### **ESC - Thoát nhanh**
```
Nhấn ESC:
✓ Thoát chương trình
✓ Xử lý 256 frame
✓ Camera mode hoàn tất

Quay lại Menu...
```

### Bước 4: Kết thúc Mode Webcam

```
Nhấn Q hoặc ESC để thoát...

✓ Thoát chương trình
✓ Xử lý 512 frame
✓ Camera mode hoàn tất

═══════════════════════════════════════════════════════════════
  Face Detection System v1.0.0
═══════════════════════════════════════════════════════════════

┌─ MENU CHÍNH ──────────────────────────────┐
│                                           │
│  [1] Phát hiện khuôn mặt từ ảnh tĩnh     │
│  [2] Phát hiện khuôn mặt từ webcam       │
│  [0] Thoát chương trình                  │
│                                           │
└───────────────────────────────────────────┘

Chọn lựa chọn (0-2): _
```

---

## 3.4. Luồng Xử Lý Chi Tiết

### 3.4.1. Xử Lý Lỗi Giao Diện

#### Lỗi Khi Mở Ảnh

```
Đường dẫn ảnh: invalid_path.jpg
✗ Ảnh không tìm thấy
✗ Lỗi load ảnh

Nhấn Enter để tiếp tục...

[Quay lại Menu]
```

#### Lỗi Khi Mở Camera

```
Đang mở camera...
✗ Lỗi mở camera
✗ Lỗi: Cannot open camera device

Nhấn Enter để tiếp tục...

[Quay lại Menu]
```

#### Lựa Chọn Không Hợp Lệ

```
Chọn lựa chọn (0-2): 5
✗ Lựa chọn không hợp lệ

Nhấn Enter để tiếp tục...

[Hiển thị Menu lại]
```

#### Thư Mục Images Trống

```
┌─ MODE ẢNH TĨNH ────────────────────────────┐
│ Nhập đường dẫn ảnh hoặc để trống để chọn   │
│ từ thư mục 'images'                        │
│ Nhập Q để quay lại menu                    │
└────────────────────────────────────────────┘

✗ Không có ảnh trong thư mục 'images'

Nhấn Enter để tiếp tục...

[Quay lại Menu]
```

---

### 3.4.2. Thông Báo Thành Công

```
✓ Ứng dụng khởi tạo thành công
✓ Detector khởi tạo
✓ Image processor khởi tạo
✓ Camera manager khởi tạo
✓ Load ảnh thành công
✓ Phát hiện: 3 khuôn mặt
✓ Lưu ảnh: output/output_2025-06-01_143022.png
✓ Frame đã lưu: output/frame_2025-06-01_143045.png
✓ Bắt đầu ghi video: output/video_2025-06-01_143050.avi
✓ Dừng ghi video
✓ Tạm dừng
✓ Tiếp tục
✓ Thoát chương trình
```

---

## 3.5. Thống Kê Hiệu Năng

### Hiển Thị Trong Ứng Dụng

```
┌─ THỐNG KÊ HIỆU NĂNG ──────────────────────┐
│                                           │
│ Detection Time:    35.47 ms               │
│ FPS:               28.5 khung/giây        │
│ Faces Detected:    2 khuôn mặt            │
│ Largest Face:      95 × 110 pixels        │
│ Smallest Face:     70 × 85 pixels         │
│ Total Area:        18,550 pixels²         │
│ Frames Processed:  512 frame              │
│                                           │
└───────────────────────────────────────────┘
```

### Log File

**Đường dẫn:** `logs/face_detection.log`

```
2025-06-01 14:30:22,123 - root - INFO - ==================================================
2025-06-01 14:30:22,123 - root - INFO - Khởi động Face Detection System v1.0.0
2025-06-01 14:30:22,123 - root - INFO - ==================================================
2025-06-01 14:30:22,456 - root - INFO - Khởi tạo ứng dụng...
2025-06-01 14:30:22,789 - detector - INFO - ✓ FaceDetector khởi tạo thành công
2025-06-01 14:30:23,012 - image_processor - INFO - ✓ ImageProcessor khởi tạo thành công
2025-06-01 14:30:23,234 - camera - INFO - ✓ CameraManager khởi tạo thành công
2025-06-01 14:30:23,567 - root - INFO - ✓ Ứng dụng khởi tạo thành công
2025-06-01 14:30:30,123 - main - INFO - ==================================================
2025-06-01 14:30:30,123 - main - INFO - MỘT TRONG CÁC ÔN IMAGE MODE
2025-06-01 14:30:30,123 - main - INFO - ==================================================
2025-06-01 14:30:35,456 - detector - DEBUG - ✓ Load cascade từ: haarcascade_frontalface_default.xml
2025-06-01 14:30:35,789 - detector - DEBUG - Ảnh grayscale: (1080, 1440, 3)
2025-06-01 14:30:36,012 - detector - DEBUG - Phát hiện 3 khuôn mặt (thời gian: 45.23ms)
2025-06-01 14:30:36,345 - detector - DEBUG - Sau NMS: 3 khuôn mặt
2025-06-01 14:30:36,678 - detector - DEBUG - Vẽ 3 khuôn mặt trên ảnh
2025-06-01 14:30:36,789 - main - INFO - ✓ Mode ảnh tĩnh hoàn tất
```

---

## 3.6. Đầu Vào và Đầu Ra

### Đầu Vào (Input)

#### Từ Ảnh Tĩnh
- **Format hỗ trợ:** `.jpg`, `.jpeg`, `.png`, `.bmp`
- **Kích thước:** Không giới hạn (từ 640×480 đến 4K+)
- **Nơi lưu trữ:** Thư mục `images/`

```
images/
├── photo1.jpg (1920×1080)
├── photo2.png (3840×2160)
├── photo3.bmp (1024×768)
└── ...
```

#### Từ Webcam
- **Độ phân giải:** 640×480 (có thể thay đổi trong `config.py`)
- **Frame rate:** 30 FPS (có thể điều chỉnh)
- **Định dạng frame:** BGR (OpenCV format)

### Đầu Ra (Output)

#### Ảnh Kết Quả
```
output/
├── output_2025-06-01_143022.png  (ảnh từ mode tĩnh)
├── frame_2025-06-01_143045.png   (frame từ mode webcam)
└── ...
```

**Định dạng tên file:** `{type}_{YYYY-MM-DD}_{HHMMSS}.{ext}`
- `type`: "output", "frame", "video"
- `{YYYY-MM-DD}_{HHMMSS}`: Timestamp (năm-tháng-ngày_giờ phút giây)
- `ext`: Phần mở rộng (.png, .jpg, .avi)

#### Video Ghi Lại
```
output/
├── video_2025-06-01_143050.avi   (512 frames, 17 giây @ 30 FPS)
└── ...
```

**Thông số video:**
- **Codec:** MJPG (Motion JPEG)
- **Frame rate:** 30 FPS
- **Độ phân giải:** 640×480
- **Duration:** Phụ thuộc số frame ghi lại

#### Log File
```
logs/
└── face_detection.log
```

---

## 3.7. Cấu Hình Giao Diện

### Màu sắc (BGR format)

```python
FACE_COLOR = (0, 255, 0)      # Xanh lục - khung khuôn mặt
TEXT_COLOR = (255, 0, 0)      # Xanh dương - text thông tin
BACKGROUND = (0, 0, 0)        # Đen - nền
```

### Kích thước Font

```python
FONT_SCALE = 0.6              # Kích thước chữ
FONT_THICKNESS = 1            # Độ dày chữ
RECTANGLE_THICKNESS = 2       # Độ dày khung
```

### Thông Số Detection

```python
SCALE_FACTOR = 1.1            # Hệ số giảm kích thước
MIN_NEIGHBORS = 5             # Số láng giềng tối thiểu
MIN_FACE_SIZE = (30, 30)      # Kích thước tối thiểu
MAX_FACE_SIZE = (500, 500)    # Kích thước tối đa
IOU_THRESHOLD = 0.3           # NMS threshold
```

---

## 3.8. Hướng Dẫn Sử Dụng Nhanh

### Mode Ảnh Tĩnh

```
1. Chạy: python main.py
2. Chọn: [1] Phát hiện khuôn mặt từ ảnh tĩnh
3. Chọn ảnh từ danh sách hoặc nhập đường dẫn
4. Xem kết quả
5. Chọn lưu ảnh (y/n)
6. Nhấn phím để tiếp tục
7. Quay lại menu
```

### Mode Webcam

```
1. Chạy: python main.py
2. Chọn: [2] Phát hiện khuôn mặt từ webcam
3. Xem feed real-time
4. Sử dụng phím tắt:
   - S: Lưu frame
   - V: Ghi video
   - P: Tạm dừng
   - Q: Thoát
5. Quay lại menu
```

### Thoát Ứng Dụng

```
1. Từ Menu: Chọn [0] Thoát chương trình
2. Hoặc từ Mode Webcam: Nhấn Q hoặc ESC
```

---

## 3.9. Giới Hạn Hiện Tại

| Aspect | Giới hạn | Ghi chú |
|--------|----------|--------|
| **Số khuôn mặt** | Không giới hạn | Tùy độ phân giải |
| **Kích thước khuôn mặt** | 30×30 - 500×500 | Cấu hình trong `config.py` |
| **FPS** | ~25-30 | Tùy CPU |
| **Độ phân giải webcam** | 640×480 | Có thể thay đổi |
| **Định dạng video** | MJPG | Hỗ trợ codec khác qua config |
| **Độ chính xác** | 85-95% | Tùy điều kiện ánh sáng |

---

## 3.10. Khắc Phục Sự Cố

### Lỗi: "Cascade file không tìm thấy"
```
✗ Lỗi: Cascade file không hợp lệ: haarcascade_frontalface_default.xml

Giải pháp:
1. Kiểm tra file haarcascade_frontalface_default.xml có tồn tại
2. Chạy: python download_cascade.py
3. Kiểm tra đường dẫn trong config.py
```

### Lỗi: "Không thể mở webcam"
```
✗ Lỗi: Không thể mở webcam

Giải pháp:
1. Kiểm tra webcam có được kết nối
2. Kiểm tra app khác không chiếm camera
3. Kiểm tra quyền truy cập camera
4. Thay CAMERA_ID trong config.py (0 → 1)
```

### Lỗi: "Ảnh không tìm thấy"
```
✗ Ảnh không tìm thấy

Giải pháp:
1. Đặt ảnh vào thư mục images/
2. Kiểm tra định dạng: .jpg, .png, .bmp
3. Kiểm tra tên file (không có khoảng trắng lạ)
```

### Hiệu Năng Thấp (FPS < 20)
```
Giải pháp:
1. Giảm độ phân giải FRAME_WIDTH, FRAME_HEIGHT trong config.py
2. Tăng SCALE_FACTOR (1.1 → 1.3) để xử lý nhanh hơn
3. Đóng ứng dụng khác
4. Nâng cấp CPU nếu cần
```

---

## Tóm Tắt

Chương này mô tả chi tiết giao diện và trải nghiệm người dùng của Hệ thống Nhận Dạng Khuôn Mặt với OpenCV. Ứng dụng cung cấp hai chế độ chính: xử lý ảnh tĩnh và xử lý real-time từ webcam, với đầy đủ thông báo, log, và xử lý lỗi.

**Tác giả:** Trần Thành Nam  
**Phiên bản:** 1.0  
**Cập nhật:** 2025-06-01
