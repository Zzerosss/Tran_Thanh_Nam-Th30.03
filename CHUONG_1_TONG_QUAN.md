# CHƯƠNG 1: TỔNG QUAN

## 1.1 Giới thiệu

### 1.1.1 Ngôn ngữ Python

#### a) Python là gì?

Python là một ngôn ngữ lập trình thông dịch, đa mục đích và mã nguồn mở. Nó được thiết kế với ưu tiên đọc dễ hiểu và cú pháp gọn nhẹ, giúp người lập trình tập trung vào giải quyết vấn đề thay vì mất thời gian vào cú pháp phức tạp.

#### b) Lịch sử phát triển

- **1989-1991:** Python được tạo ra bởi Guido van Rossum tại CWI (Centrum Wiskunde & Informatica) ở Hà Lan. Phiên bản đầu tiên, Python 0.9.0, được phát hành vào tháng 2 năm 1991.

- **1994:** Python 1.0 ra mắt với nhiều tính năng mới như lambda, map, filter, và reduce.

- **2000:** Python 2.0 giới thiệu Garbage Collection và hỗ trợ Unicode. Python ngày càng trở nên phổ biến, đặc biệt trong cộng đồng lập trình web.

- **2008:** Python 3.0 (hay Python 3000 hoặc "Py3k") được phát hành, với sự thay đổi lớn trong cú pháp và thiết kế để cải thiện sự đơn giản, đồng thời giữ lại sự tương thích ngược với Python 2.

- **Ngày nay:** Python đã trở thành một trong những ngôn ngữ lập trình phổ biến nhất thế giới, được sử dụng rộng rãi trong nhiều lĩnh vực như phân tích dữ liệu, trí tuệ nhân tạo, phát triển web, và hệ thống.

#### c) Đặc điểm nổi bật của Python

- **Dễ đọc và dễ hiểu:** Cú pháp của Python tập trung vào sự đơn giản và rõ ràng, giúp người lập trình tập trung vào giải quyết vấn đề thay vì cú pháp phức tạp.

- **Mã nguồn mở:** Python có giấy phép mã nguồn mở, khuyến khích sự hợp tác và đóng góp từ cộng đồng.

- **Đa mục đích:** Python có thể sử dụng cho mọi thứ từ lập trình web, phân tích dữ liệu, trí tuệ nhân tạo đến lập trình nhúng và đám mây.

- **Thư viện và Framework:** Python có thư viện phong phú và các framework như Django, Flask, NumPy, OpenCV, và Pandas, giúp tăng cường khả năng phát triển.

- **Cộng đồng mạnh mẽ:** Cộng đồng Python rất lớn, với hàng ngàn người đóng góp vào sự phát triển, hỗ trợ qua diễn đàn, tài liệu và đồ án môn học mã nguồn mở.

### 1.1.2 Các thư viện chính được sử dụng

#### a) OpenCV (Computer Vision Library)

OpenCV là một thư viện mã nguồn mở được thiết kế để xử lý hình ảnh và video. Nó cung cấp các công cụ mạnh mẽ cho:

- Xử lý và phân tích hình ảnh
- Phát hiện và nhận dạng khuôn mặt
- Theo dõi chuyển động
- Xử lý video thời gian thực
- Lọc ảnh và cải thiện chất lượng ảnh

OpenCV được sử dụng rộng rãi trong các ứng dụng về thị giác máy tính, an ninh, y tế, và nhiều lĩnh vực khác.

#### b) NumPy (Numerical Python)

NumPy là một thư viện Python cung cấp hỗ trợ cho các mảng và ma trận đa chiều, cùng với một tập hợp lớn các hàm toán học để hoạt động trên các mảng này. Các tính năng chính:

- Tạo và thao tác các mảng đa chiều
- Thực hiện các phép toán đại số tuyến tính
- Hỗ trợ xử lý dữ liệu khoa học
- Tối ưu hiệu năng tính toán
- Tích hợp tốt với các thư viện khác như Pandas, Matplotlib

NumPy là nền tảng cho hầu hết các thư viện khoa học và dữ liệu khác trong Python.

#### c) Pytest (Testing Framework)

Pytest là một framework kiểm thử (testing framework) được thiết kế để làm cho việc viết các bài kiểm thử đơn giản và hiệu quả. Các tính năng nổi bật:

- Cú pháp đơn giản và dễ hiểu
- Hỗ trợ tự động khám phá các bài kiểm thử
- Cho phép viết các bài kiểm thử phức tạp với ít code hơn
- Báo cáo lỗi chi tiết và rõ ràng
- Hỗ trợ fixture và plugin mở rộng
- Tích hợp tốt với các công cụ CI/CD

Pytest giúp đảm bảo chất lượng code và phát hiện lỗi sớm trong quá trình phát triển.

## 1.2 Hướng dẫn cài đặt Python và các thư viện trên Visual Studio Code

### 1.2.1 Cài đặt Python

Để cài đặt Python, bạn vào trang chủ của Python tại https://www.python.org/ và tải về phiên bản phù hợp với hệ điều hành đang dùng. 

**Lưu ý quan trọng:** Khi cài đặt Python, hãy **tích chọn** "Add Python to PATH" (Thêm Python vào biến môi trường) để có thể sử dụng Python từ dòng lệnh.

Ở đây, tôi khuyên bạn nên sử dụng Python 3.11 trở lên để đảm bảo tương thích với các thư viện mới nhất.

Để kiểm tra đã cài đặt Python thành công, bạn mở Command Prompt (Windows + R, gõ cmd) và gõ lệnh:
```bash
python --version
```

Nếu hiển thị phiên bản Python, cài đặt đã thành công.

### 1.2.2 Cài đặt Visual Studio Code

**Bước 1:** Truy cập trang chủ Visual Studio Code tại https://code.visualstudio.com/ và tải về phiên bản phù hợp với hệ điều hành.

**Bước 2:** Cài đặt theo hướng dẫn trên màn hình. Phần lớn thiết lập mặc định là phù hợp.

**Bước 3:** Sau khi cài đặt xong, mở Visual Studio Code.

**Bước 4:** Cài đặt Extension Python của Microsoft:
- Bấm vào biểu tượng Extension (Ctrl + Shift + X)
- Tìm kiếm "Python"
- Chọn "Python" của Microsoft và bấm "Install"

**Bước 5:** Cài đặt thêm Extension "Pylance" để có tính năng IntelliSense tốt hơn:
- Tìm kiếm "Pylance"
- Cài đặt extension này

### 1.2.3 Cài đặt các thư viện OpenCV, NumPy, và Pytest

#### Phương pháp 1: Sử dụng Terminal trong Visual Studio Code

**Bước 1:** Mở Visual Studio Code.

**Bước 2:** Mở Terminal bằng cách nhấn Ctrl + ` (backtick) hoặc vào menu Terminal → New Terminal.

**Bước 3:** Kiểm tra phiên bản pip:
```bash
pip --version
```

**Bước 4:** Cập nhật pip lên phiên bản mới nhất (tùy chọn):
```bash
python -m pip install --upgrade pip
```

**Bước 5:** Cài đặt OpenCV:
```bash
pip install opencv-python
```

**Bước 6:** Cài đặt NumPy:
```bash
pip install numpy
```

**Bước 7:** Cài đặt Pytest:
```bash
pip install pytest
```

**Bước 8:** Cài đặt tất cả cùng lúc:
```bash
pip install opencv-python numpy pytest
```

#### Phương pháp 2: Sử dụng file requirements.txt

**Bước 1:** Tạo file `requirements.txt` trong thư mục dự án của bạn.

**Bước 2:** Mở file `requirements.txt` và thêm nội dung sau:
```
opencv-python==4.8.1.78
numpy==1.24.3
pytest==7.4.0
```

**Bước 3:** Mở Terminal trong Visual Studio Code (Ctrl + `).

**Bước 4:** Gõ lệnh:
```bash
pip install -r requirements.txt
```

### 1.2.4 Kiểm tra cài đặt

Sau khi cài đặt xong các thư viện, bạn có thể kiểm tra chúng bằng cách:

**Bước 1:** Tạo file `test_install.py` trong thư mục dự án.

**Bước 2:** Thêm nội dung sau:
```python
# Kiểm tra các thư viện
import cv2
import numpy as np
import pytest

print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)
print("Pytest version:", pytest.__version__)
print("\n✓ Tất cả các thư viện đã cài đặt thành công!")
```

**Bước 3:** Bấm chuột phải vào file và chọn "Run Python File in Terminal" hoặc nhấn Ctrl + F5.

Nếu kết quả hiển thị các phiên bản của các thư viện, việc cài đặt đã hoàn tất thành công.

### 1.2.5 Cấu hình Visual Studio Code cho Python

#### Thiết lập Formatter (Định dạng Code)

**Bước 1:** Mở Settings (Ctrl + ,).

**Bước 2:** Tìm kiếm "Python Formatting Provider".

**Bước 3:** Chọn "black" hoặc "autopep8" làm formatter mặc định.

**Bước 4:** Tìm kiếm "Format On Save" và tích chọn để tự động định dạng code khi lưu file.

#### Thiết lập Linter (Kiểm tra Lỗi)

**Bước 1:** Cài đặt pylint:
```bash
pip install pylint
```

**Bước 2:** Mở Settings (Ctrl + ,).

**Bước 3:** Tìm kiếm "Python Linting Enabled" và tích chọn.

**Bước 4:** Tìm kiếm "Python Linting Pylint Enabled" và tích chọn.

### 1.2.6 Một số Shortcut hữu ích trong Visual Studio Code

| Shortcut | Chức năng |
|----------|---------|
| Ctrl + ` | Mở/Đóng Terminal |
| Ctrl + / | Bình luận/Bỏ bình luận dòng |
| Ctrl + Shift + P | Mở Command Palette |
| Ctrl + F5 | Chạy Python File |
| F5 | Debug |
| Ctrl + B | Ẩn/Hiện Sidebar |
| Ctrl + D | Chọn từ tương tự tiếp theo |
| Ctrl + L | Chọn toàn bộ dòng |
| Alt + Up/Down | Di chuyển dòng lên/xuống |
| Ctrl + Alt + Up/Down | Nhân bản dòng lên/xuống |

## 1.3 Tạo Dự án Python đầu tiên

### 1.3.1 Tạo thư mục dự án

**Bước 1:** Tạo một thư mục mới cho dự án của bạn trên máy tính. Ví dụ: `MyPythonProject`

**Bước 2:** Mở thư mục này bằng Visual Studio Code:
- File → Open Folder → Chọn thư mục vừa tạo

### 1.3.2 Tạo file Python đầu tiên

**Bước 1:** Trong Visual Studio Code, bấm Ctrl + N để tạo file mới.

**Bước 2:** Lưu file với tên `main.py` (Ctrl + S).

**Bước 3:** Thêm đoạn code đơn giản:
```python
# Chương trình Python đầu tiên
print("Xin chào, đây là chương trình Python của tôi!")
print("OpenCV, NumPy, và Pytest đã sẵn sàng!")
```

**Bước 4:** Chạy chương trình bằng cách bấm Ctrl + F5 hoặc chuột phải chọn "Run Python File in Terminal".

Chúc mừng! Bạn đã hoàn thành thiết lập môi trường Python trên Visual Studio Code và sẵn sàng bắt đầu phát triển các ứng dụng Python!

---

**Ghi chú:** Nếu bạn gặp bất kỳ lỗi nào trong quá trình cài đặt hoặc chạy chương trình, hãy kiểm tra lại các bước trên hoặc tham khảo tài liệu chính thức của từng thư viện.
