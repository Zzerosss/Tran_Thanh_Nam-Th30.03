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

- **Thư viện và Framework:** Python có thư viện phong phú và các framework như Django, Flask, NumPy, và Pandas, giúp tăng cường khả năng phát triển.

- **Cộng đồng mạnh mẽ:** Cộng đồng Python rất lớn, với hàng ngàn người đóng góp vào sự phát triển, hỗ trợ qua diễn đàn, tài liệu và đồ án môn học mã nguồn mở.

### 1.1.2 Thư viện Pygame

#### a) Giới thiệu chung

Pygame là một thư viện lập trình game cho Python, được xây dựng trên nền tảng Simple DirectMedia Layer (SDL). Nó cung cấp các công cụ và chức năng để phát triển trò chơi đồ họa 2D một cách đơn giản và linh hoạt. Pygame giúp người lập trình tạo ra các trải nghiệm game mà không cần mất nhiều thời gian và công sức.

#### b) Đặc điểm nổi bật

- **Dễ Học và Sử Dụng:** Pygame được thiết kế để làm cho việc phát triển trò chơi đơn giản và dễ tiếp cận cho người mới học lập trình.

- **Đồ Họa 2D:** Pygame chủ yếu được sử dụng cho phát triển trò chơi đồ họa 2D, với khả năng xử lý sprite, hình ảnh, và âm thanh.

- **Sử Dụng SDL:** SDL là một thư viện đa nền tảng (cross-platform) giúp tương tác với phần cứng máy tính, điều này làm cho Pygame có khả năng chạy trên nhiều hệ điều hành khác nhau.

- **Thư Viện Mạnh Mẽ:** Pygame đi kèm với nhiều thư viện hỗ trợ cho đồ họa, âm thanh, đầu vào từ bàn phím và chuột, giúp đơn giản hóa việc phát triển game.

- **Cộng Đồng Hoạt Động:** Pygame có một cộng đồng sôi nổi với nhiều tài nguyên, hướng dẫn và ví dụ trực tuyến giúp người lập trình giải quyết vấn đề và phát triển kỹ năng.

#### c) Các phần chính của Pygame

- **pygame.display:** Quản lý cửa sổ hiển thị game.

- **pygame.sprite:** Hỗ trợ quản lý sprite và collision detection.

- **pygame.image:** Cho phép làm việc với hình ảnh.

- **pygame.mixer:** Điều khiển âm thanh và âm nhạc.

- **pygame.event:** Xử lý sự kiện từ bàn phím, chuột, và các nguồn khác.

- **pygame.font:** Cho phép vẽ văn bản trực tiếp trên cửa sổ game.

## 1.2 Hướng dẫn cài đặt Python và thư viện Pygame

### 1.2.1 Cài đặt Python

Để cài đặt Python, bạn vào trang chủ của Python tại https://python.org/ và tải về phiên bản phù hợp với hệ điều hành đang dùng. Ở đây tôi không đi vào chi tiết cách cài đặt, cá nhân tôi sử dụng phiên bản 3.11 cho Windows 64 bit và cài vào thư mục C:\Python11, chỉ lưu ý các bạn khi cài đặt nên tích chọn để đưa Python vào biến môi trường (System Path). 

Nếu không, bạn phải thêm thư mục Python vào System Path một cách thủ công như sau:

**Bước 1:** Bấm chuột phải vào My Computer (hoặc This PC) ngoài Desktop và chọn Properties; hoặc bấm tổ hợp phím Windows + Break; hoặc vào Control Panel\System and Security\System.

**Bước 2:** Chọn thẻ Advanced System Setting để mở hộp thoại System Properties.

**Bước 3:** Chọn thẻ Advanced rồi chọn nút Environment Variables…

**Bước 4:** Trong thẻ System variables, chọn dòng Path và bấm Edit.

**Bước 5:** Tiếp tục chọn New và gõ vào đường dẫn đến thư mục cài đặt Python, ở đây, của tôi là:
```
C:\Users\hau66\AppData\Local\Programs\Python\Python311
```

**Bước 6:** Chọn tiếp New và thêm tiếp thư mục chứa các Scripts, ở đây, máy của tôi là:
```
C:\Users\hau66\AppData\Local\Programs\Python\Python311\Scripts
```

**Bước 7:** Bấm OK.

Để kiểm tra đã thêm Python vào System Path chưa, bạn mở hộp thoại Run của Windows (Windows + R) và gõ `python`, sau đó bấm Enter. Nếu hiện cửa sổ Python interpreter là thành công.

Sau khi cài đặt xong trình biên dịch Python, mặc định sẽ có một trình soạn thảo đi kèm là IDLE, tuy nhiên trình soạn thảo này khá cơ bản và không hỗ trợ nhiều cho người sử dụng như gợi ý các từ khóa, quản lý project, gỡ lỗi… nên tôi khuyên bạn nên sử dụng thêm một trình soạn thảo như Notepad++, Sublime Text, Visual Studio Code, Pycharm, Eclipse… Có rất nhiều chương trình như vậy, cả miễn phí và trả phí, nhưng cá nhân tôi thường sử dụng Visual Studio Code của Microsoft, đôi khi cũng sử dụng thêm cả Sublime Text 3.

Nếu mới làm quen với Python, bạn có thể cài đặt Anaconda tại https://www.continuum.io là một môi trường Python đã bao gồm cả trình dịch Python, trình soạn thảo với rất nhiều tính năng cao cấp chuyên dụng giành cho Data Science, và được cài sẵn rất nhiều thư viện, đặc biệt là các thư viện cho Machine Learning, Data Science như numpy, jupyter, matplotlib...

**Ví dụ:** chạy một chương trình python bằng Visual Studio Code bấm chuột phải vào vùng soạn thảo và chọn "Run Python File in Terminal".

### 1.2.2 Cài đặt thư viện Pygame

Để cài đặt Pygame trên máy tính của bạn, bạn có thể sử dụng pip, trình quản lý gói Python. Ở đây chỉ hướng dẫn cách cài thư viện trên hệ điều hành Windows.

**Bước 1:** Bạn mở hộp thoại Run (Windows + R) và gõ lệnh `cmd`.

**Bước 2:** Trong hộp thoại Cmd bạn gõ lệnh:
```bash
pip install pygame
```
Sau đó nhấn Enter.

**Bước 3:** Đợi cho đến khi cài đặt hoàn tất. Quá trình này có thể mất vài phút tùy thuộc vào tốc độ Internet của bạn.

Sau đó để kiểm tra đã cài đặt pygame chưa, bạn có thể tạo một script Python và chạy đoạn code sau:

```python
import pygame
print("Pygame version:", pygame.__version__)
print("Pygame cài đặt thành công!")
```

Nếu script chạy mà không có lỗi và in ra phiên bản của Pygame, điều đó có nghĩa là bạn đã cài đặt pygame thành công. Nếu có lỗi, hãy kiểm tra lại các bước trên hoặc tham khảo tài liệu chính thức của Pygame tại https://www.pygame.org/docs/

---

**Ghi chú:** Nếu bạn muốn cài đặt nhiều thư viện cùng lúc, bạn có thể tạo một file `requirements.txt` chứa danh sách các thư viện và dùng lệnh:
```bash
pip install -r requirements.txt
```
