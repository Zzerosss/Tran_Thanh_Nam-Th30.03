# -*- coding: utf-8 -*-
"""
Module tiện ích (utils.py)
====================================
Các hàm tiện ích dùng chung: logging, error handling, conversion, validation.

Chức năng:
- Setup logging
- Xử lý lỗi
- Kiểm tra file tồn tại
- Chuyển đổi định dạng
- Tính toán FPS
- Lưu file

Tác giả: Trần Thành Nam
Phiên bản: 1.0
"""

import logging
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, List
import cv2
import numpy as np

import config

# ========== SETUP LOGGER ==========
logger = logging.getLogger(__name__)


def setup_logging() -> logging.Logger:
    """
    Cấu hình hệ thống logging cho ứng dụng.
    
    Returns:
        logging.Logger: Logger object được cấu hình
    
    Ví dụ:
        logger = setup_logging()
        logger.info("Ứng dụng khởi động")
    """
    # Tạo thư mục logs nếu chưa tồn tại
    os.makedirs(config.LOGS_DIR, exist_ok=True)
    
    # Cấu hình logger chính
    logger = logging.getLogger("FaceDetection")
    logger.setLevel(getattr(logging, config.LOG_LEVEL))
    
    # Formatter
    formatter = logging.Formatter(config.LOG_FORMAT)
    
    # Handler file
    file_handler = logging.FileHandler(config.LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


# ========== HÀM KIỂM TRA ==========
def file_exists(filepath: str) -> bool:
    """
    Kiểm tra file có tồn tại hay không.
    
    Args:
        filepath (str): Đường dẫn file cần kiểm tra
    
    Returns:
        bool: True nếu file tồn tại, False nếu không
    """
    return os.path.isfile(filepath)


def directory_exists(dirpath: str) -> bool:
    """
    Kiểm tra thư mục có tồn tại hay không.
    
    Args:
        dirpath (str): Đường dẫn thư mục cần kiểm tra
    
    Returns:
        bool: True nếu thư mục tồn tại, False nếu không
    """
    return os.path.isdir(dirpath)


def is_valid_image(filepath: str) -> bool:
    """
    Kiểm tra file ảnh có hợp lệ hay không.
    
    Args:
        filepath (str): Đường dẫn file ảnh
    
    Returns:
        bool: True nếu file ảnh hợp lệ, False nếu không
    """
    if not file_exists(filepath):
        logger.warning(f"Ảnh không tồn tại: {filepath}")
        return False
    
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    file_extension = Path(filepath).suffix.lower()
    
    if file_extension not in valid_extensions:
        logger.warning(f"Định dạng ảnh không hỗ trợ: {filepath}")
        return False
    
    # Thử load ảnh để kiểm tra
    img = cv2.imread(filepath)
    if img is None:
        logger.warning(f"Không thể load ảnh: {filepath}")
        return False
    
    return True


def is_valid_cascade(cascade_path: str) -> bool:
    """
    Kiểm tra file Haar Cascade có hợp lệ hay không.
    
    Args:
        cascade_path (str): Đường dẫn file cascade
    
    Returns:
        bool: True nếu file cascade hợp lệ, False nếu không
    """
    if not file_exists(cascade_path):
        logger.error(f"Cascade không tìm thấy: {cascade_path}")
        return False
    
    try:
        cascade = cv2.CascadeClassifier(cascade_path)
        if cascade.empty():
            logger.error(f"Cascade rỗng: {cascade_path}")
            return False
    except Exception as e:
        logger.error(f"Lỗi load cascade: {e}")
        return False
    
    return True


# ========== HÀM CHUYỂN ĐỔI ==========
def bgr_to_rgb(image: np.ndarray) -> np.ndarray:
    """
    Chuyển đổi ảnh từ định dạng BGR sang RGB.
    
    Args:
        image (np.ndarray): Ảnh input (BGR)
    
    Returns:
        np.ndarray: Ảnh output (RGB)
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def rgb_to_bgr(image: np.ndarray) -> np.ndarray:
    """
    Chuyển đổi ảnh từ định dạng RGB sang BGR.
    
    Args:
        image (np.ndarray): Ảnh input (RGB)
    
    Returns:
        np.ndarray: Ảnh output (BGR)
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Chuyển ảnh sang thang xám (Grayscale).
    
    Args:
        image (np.ndarray): Ảnh input (BGR)
    
    Returns:
        np.ndarray: Ảnh thang xám
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    if len(image.shape) == 2:  # Đã là thang xám
        return image
    
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# ========== HÀM RESIZE ==========
def resize_image(image: np.ndarray, scale: float = 0.5) -> np.ndarray:
    """
    Thay đổi kích thước ảnh theo scale.
    
    Args:
        image (np.ndarray): Ảnh input
        scale (float): Tỷ lệ thay đổi (0-1)
    
    Returns:
        np.ndarray: Ảnh sau khi resize
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    if scale <= 0 or scale > 1:
        logger.warning(f"Scale không hợp lệ: {scale}, sử dụng scale=0.5")
        scale = 0.5
    
    height, width = image.shape[:2]
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    resized = cv2.resize(image, (new_width, new_height))
    logger.debug(f"Resize ảnh từ ({width}x{height}) sang ({new_width}x{new_height})")
    
    return resized


def resize_to_resolution(image: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    Resize ảnh về kích thước cụ thể.
    
    Args:
        image (np.ndarray): Ảnh input
        width (int): Chiều rộng mong muốn
        height (int): Chiều cao mong muốn
    
    Returns:
        np.ndarray: Ảnh sau khi resize
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    return cv2.resize(image, (width, height))


# ========== HÀM LƯU TRỮ ==========
def save_image(image: np.ndarray, output_path: str, create_dir: bool = True) -> bool:
    """
    Lưu ảnh vào file.
    
    Args:
        image (np.ndarray): Ảnh cần lưu
        output_path (str): Đường dẫn output
        create_dir (bool): Có tạo thư mục nếu chưa tồn tại
    
    Returns:
        bool: True nếu lưu thành công, False nếu lỗi
    """
    if image is None or image.size == 0:
        logger.error("Ảnh đầu vào trống, không thể lưu")
        return False
    
    try:
        # Tạo thư mục nếu cần
        if create_dir:
            output_dir = os.path.dirname(output_path)
            os.makedirs(output_dir, exist_ok=True)
        
        # Lưu file
        success = cv2.imwrite(output_path, image)
        
        if success:
            logger.info(f"✓ Lưu ảnh thành công: {output_path}")
            return True
        else:
            logger.error(f"✗ Lỗi lưu ảnh: {output_path}")
            return False
    
    except Exception as e:
        logger.error(f"✗ Exception lưu ảnh: {e}")
        return False


def generate_output_filename(prefix: str = "detected", extension: str = ".jpg") -> str:
    """
    Tạo tên file output duy nhất.
    
    Args:
        prefix (str): Tiền tố tên file
        extension (str): Phần mở rộng file
    
    Returns:
        str: Tên file output đầy đủ
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:16]
    filename = f"{prefix}_{timestamp}{extension}"
    filepath = os.path.join(config.OUTPUT_DIR, filename)
    
    logger.debug(f"Tạo tên file output: {filepath}")
    return filepath


# ========== HÀM TÍNH TOÁN ==========
class FPSCounter:
    """
    Lớp tính toán và theo dõi FPS (Frames Per Second).
    
    Thuộc tính:
        start_time (float): Thời điểm bắt đầu
        frames (int): Số frame đã xử lý
        avg_fps (float): FPS trung bình
    
    Phương thức:
        update(): Cập nhật một frame
        get_fps(): Lấy FPS hiện tại
        reset(): Đặt lại bộ đếm
    """
    
    def __init__(self, average_count: int = 30):
        """
        Khởi tạo FPS counter.
        
        Args:
            average_count (int): Số frame dùng để tính trung bình
        """
        self.average_count = average_count
        self.frame_times = []
        self.avg_fps = 0
        self.start_time = datetime.now()
    
    def update(self) -> None:
        """Cập nhật một frame mới."""
        current_time = datetime.now()
        self.frame_times.append(current_time)
        
        # Giữ chỉ average_count frame gần nhất
        if len(self.frame_times) > self.average_count:
            self.frame_times.pop(0)
    
    def get_fps(self) -> float:
        """
        Tính toán FPS hiện tại.
        
        Returns:
            float: FPS hiện tại
        """
        if len(self.frame_times) < 2:
            return 0.0
        
        time_diff = (self.frame_times[-1] - self.frame_times[0]).total_seconds()
        
        if time_diff == 0:
            return 0.0
        
        self.avg_fps = (len(self.frame_times) - 1) / time_diff
        return self.avg_fps
    
    def reset(self) -> None:
        """Đặt lại bộ đếm."""
        self.frame_times = []
        self.avg_fps = 0
        self.start_time = datetime.now()


# ========== HÀM HIỂN THỊ ==========
def put_text(image: np.ndarray, text: str, position: Tuple[int, int],
             font_scale: float = 0.6, thickness: int = 1,
             color: Tuple[int, int, int] = (255, 0, 0)) -> np.ndarray:
    """
    Vẽ chữ lên ảnh.
    
    Args:
        image (np.ndarray): Ảnh input
        text (str): Nội dung text
        position (Tuple[int, int]): Vị trí (x, y)
        font_scale (float): Kích thước font
        thickness (int): Độ dày chữ
        color (Tuple[int, int, int]): Màu (BGR)
    
    Returns:
        np.ndarray: Ảnh sau khi vẽ chữ
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX,
                font_scale, color, thickness, cv2.LINE_AA)
    
    return image


def put_rectangle(image: np.ndarray, x: int, y: int, w: int, h: int,
                  color: Tuple[int, int, int] = (0, 255, 0),
                  thickness: int = 2) -> np.ndarray:
    """
    Vẽ hình chữ nhật lên ảnh.
    
    Args:
        image (np.ndarray): Ảnh input
        x (int): Tọa độ x
        y (int): Tọa độ y
        w (int): Chiều rộng
        h (int): Chiều cao
        color (Tuple[int, int, int]): Màu (BGR)
        thickness (int): Độ dày đường
    
    Returns:
        np.ndarray: Ảnh sau khi vẽ
    """
    if image is None or image.size == 0:
        logger.warning("Ảnh đầu vào trống")
        return image
    
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(image, pt1, pt2, color, thickness)
    
    return image


# ========== HÀM LỲI ==========
def calculate_iou(box1: Tuple[int, int, int, int], 
                  box2: Tuple[int, int, int, int]) -> float:
    """
    Tính Intersection over Union (IoU) giữa hai bounding box.
    
    Args:
        box1 (Tuple): (x, y, width, height)
        box2 (Tuple): (x, y, width, height)
    
    Returns:
        float: IoU value (0-1)
    """
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    
    # Tính giao điểm
    xi1 = max(x1, x2)
    yi1 = max(y1, y2)
    xi2 = min(x1 + w1, x2 + w2)
    yi2 = min(y1 + h1, y2 + h2)
    
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    
    # Tính union
    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - inter_area
    
    if union_area == 0:
        return 0.0
    
    iou = inter_area / union_area
    return iou


def get_image_info(image: np.ndarray) -> dict:
    """
    Lấy thông tin chi tiết về ảnh.
    
    Args:
        image (np.ndarray): Ảnh cần kiểm tra
    
    Returns:
        dict: Thông tin ảnh (width, height, channels, dtype, size)
    """
    if image is None or image.size == 0:
        return {}
    
    height, width = image.shape[:2]
    channels = image.shape[2] if len(image.shape) == 3 else 1
    
    info = {
        'width': width,
        'height': height,
        'channels': channels,
        'dtype': str(image.dtype),
        'size_bytes': image.nbytes,
        'size_mb': image.nbytes / (1024 * 1024),
        'aspect_ratio': width / height if height != 0 else 0
    }
    
    return info


if __name__ == "__main__":
    # Test các hàm tiện ích
    logger = setup_logging()
    logger.info("✓ Khởi tạo logging thành công")
    
    # Test kiểm tra file
    print(f"Cascade tồn tại: {file_exists(config.CASCADE_PATH)}")
    
    # Test FPS counter
    fps_counter = FPSCounter()
    for i in range(30):
        fps_counter.update()
    
    print(f"FPS: {fps_counter.get_fps():.2f}")
    print(f"✓ Tất cả test hoàn tất!")
