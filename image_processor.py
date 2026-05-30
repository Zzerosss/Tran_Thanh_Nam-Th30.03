# -*- coding: utf-8 -*-
"""
Module xử lý ảnh (image_processor.py)
====================================
Lớp ImageProcessor dùng để tải, xử lý, và lưu ảnh.

Chức năng:
- Tải ảnh từ file
- Resize ảnh
- Convert định dạng màu
- Hiển thị ảnh
- Lưu ảnh
- Lấy thông tin ảnh

Tác giả: Trần Thành Nam
Phiên bản: 1.0
"""

import logging
from typing import Optional, Tuple
from pathlib import Path
import numpy as np
import cv2

import config
import utils

logger = logging.getLogger(__name__)


class ImageProcessor:
    """
    Lớp xử lý ảnh.
    
    Thuộc tính:
        image_path (str): Đường dẫn ảnh input
        original_image (np.ndarray): Ảnh gốc
        processed_image (np.ndarray): Ảnh đã xử lý
        image_info (dict): Thông tin ảnh
    
    Phương thức:
        load_image(): Tải ảnh từ file
        resize_image(): Thay đổi kích thước
        convert_to_grayscale(): Chuyển sang thang xám
        save_image(): Lưu ảnh
        display_image(): Hiển thị ảnh
        get_image_info(): Lấy thông tin ảnh
    """
    
    def __init__(self, image_path: Optional[str] = None):
        """
        Khởi tạo ImageProcessor.
        
        Args:
            image_path (str): Đường dẫn ảnh (tùy chọn)
        
        Ví dụ:
            processor = ImageProcessor("images/photo.jpg")
            processor = ImageProcessor()  # Khởi tạo rỗng
        """
        logger.info("Khởi tạo ImageProcessor...")
        
        self.image_path = image_path
        self.original_image: Optional[np.ndarray] = None
        self.processed_image: Optional[np.ndarray] = None
        self.image_info = {}
        
        # Tải ảnh nếu cung cấp đường dẫn
        if image_path:
            self.load_image(image_path)
        
        logger.info("✓ ImageProcessor khởi tạo thành công")
    
    def load_image(self, image_path: str) -> bool:
        """
        Tải ảnh từ file.
        
        Args:
            image_path (str): Đường dẫn file ảnh
        
        Returns:
            bool: True nếu tải thành công, False nếu lỗi
        
        Ví dụ:
            processor = ImageProcessor()
            if processor.load_image("photo.jpg"):
                print("✓ Ảnh được tải thành công")
        """
        logger.info(f"Đang tải ảnh từ: {image_path}")
        
        # Kiểm tra file tồn tại
        if not utils.is_valid_image(image_path):
            logger.error(f"✗ Ảnh không hợp lệ: {image_path}")
            return False
        
        try:
            # Tải ảnh
            image = cv2.imread(image_path)
            
            if image is None:
                logger.error(f"✗ Lỗi tải ảnh: {image_path}")
                return False
            
            # Lưu trữ
            self.image_path = image_path
            self.original_image = image.copy()
            self.processed_image = image.copy()
            
            # Lấy thông tin ảnh
            self.image_info = utils.get_image_info(image)
            
            logger.info(f"✓ Tải ảnh thành công: {image_path}")
            logger.debug(f"Kích thước: {self.image_info['width']}x{self.image_info['height']}")
            
            return True
        
        except Exception as e:
            logger.error(f"✗ Exception tải ảnh: {e}")
            return False
    
    def get_original_image(self) -> Optional[np.ndarray]:
        """
        Lấy ảnh gốc.
        
        Returns:
            np.ndarray hoặc None: Ảnh gốc
        """
        return self.original_image.copy() if self.original_image is not None else None
    
    def get_processed_image(self) -> Optional[np.ndarray]:
        """
        Lấy ảnh đã xử lý.
        
        Returns:
            np.ndarray hoặc None: Ảnh đã xử lý
        """
        return self.processed_image.copy() if self.processed_image is not None else None
    
    def reset_to_original(self) -> bool:
        """
        Đặt lại ảnh về trạng thái gốc.
        
        Returns:
            bool: True nếu thành công
        """
        if self.original_image is None:
            logger.warning("Không có ảnh gốc để reset")
            return False
        
        self.processed_image = self.original_image.copy()
        logger.info("✓ Reset ảnh về trạng thái gốc")
        return True
    
    def resize_image(self, scale: float = 0.5) -> bool:
        """
        Resize ảnh theo scale.
        
        Args:
            scale (float): Tỷ lệ resize (0-1)
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            processor.resize_image(0.8)  # Resize xuống 80%
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để resize")
            return False
        
        if scale <= 0 or scale > 1:
            logger.warning(f"Scale không hợp lệ: {scale}")
            return False
        
        try:
            self.processed_image = utils.resize_image(self.processed_image, scale)
            logger.info(f"✓ Resize ảnh theo scale: {scale}")
            return True
        
        except Exception as e:
            logger.error(f"✗ Lỗi resize: {e}")
            return False
    
    def resize_to_resolution(self, width: int, height: int) -> bool:
        """
        Resize ảnh về kích thước cụ thể.
        
        Args:
            width (int): Chiều rộng mong muốn
            height (int): Chiều cao mong muốn
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            processor.resize_to_resolution(640, 480)
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để resize")
            return False
        
        try:
            self.processed_image = utils.resize_to_resolution(
                self.processed_image, width, height
            )
            logger.info(f"✓ Resize ảnh về: {width}x{height}")
            return True
        
        except Exception as e:
            logger.error(f"✗ Lỗi resize: {e}")
            return False
    
    def convert_to_grayscale(self) -> bool:
        """
        Chuyển ảnh sang thang xám.
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            processor.convert_to_grayscale()
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để convert")
            return False
        
        try:
            self.processed_image = utils.to_grayscale(self.processed_image)
            logger.info("✓ Convert ảnh sang thang xám")
            return True
        
        except Exception as e:
            logger.error(f"✗ Lỗi convert: {e}")
            return False
    
    def convert_to_bgr(self) -> bool:
        """
        Chuyển ảnh sang định dạng BGR (nếu là RGB).
        
        Returns:
            bool: True nếu thành công
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để convert")
            return False
        
        try:
            if len(self.processed_image.shape) == 3 and \
               self.processed_image.shape[2] == 3:
                self.processed_image = utils.rgb_to_bgr(self.processed_image)
                logger.info("✓ Convert ảnh sang BGR")
            return True
        
        except Exception as e:
            logger.error(f"✗ Lỗi convert: {e}")
            return False
    
    def adjust_brightness(self, factor: float = 1.0) -> bool:
        """
        Điều chỉnh độ sáng ảnh.
        
        Args:
            factor (float): Hệ số điều chỉnh (0.5-2.0)
                          1.0 = không đổi
                          < 1.0 = tối hơn
                          > 1.0 = sáng hơn
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            processor.adjust_brightness(1.2)  # Sáng hơn 20%
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để điều chỉnh")
            return False
        
        if factor < 0.1 or factor > 3.0:
            logger.warning(f"Factor không hợp lệ: {factor}")
            return False
        
        try:
            # Điều chỉnh độ sáng
            hsv = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)
            v = cv2.multiply(v, factor)
            v = np.clip(v, 0, 255).astype(np.uint8)
            hsv = cv2.merge([h, s, v])
            self.processed_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            
            logger.info(f"✓ Điều chỉnh độ sáng: {factor}")
            return True
        
        except Exception as e:
            logger.error(f"✗ Lỗi điều chỉnh độ sáng: {e}")
            return False
    
    def apply_blur(self, kernel_size: int = 5) -> bool:
        """
        Áp dụng Gaussian Blur lên ảnh.
        
        Args:
            kernel_size (int): Kích thước kernel (phải là số lẻ)
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            processor.apply_blur(7)
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để blur")
            return False
        
        if kernel_size % 2 == 0:
            kernel_size += 1  # Đảm bảo là số lẻ
        
        try:
            self.processed_image = cv2.GaussianBlur(
                self.processed_image, (kernel_size, kernel_size), 0
            )
            logger.info(f"✓ Áp dụng blur với kernel size: {kernel_size}")
            return True
        
        except Exception as e:
            logger.error(f"✗ Lỗi blur: {e}")
            return False
    
    def save_image(self, output_path: Optional[str] = None) -> bool:
        """
        Lưu ảnh đã xử lý.
        
        Args:
            output_path (str): Đường dẫn output. Nếu None thì tạo tự động
        
        Returns:
            bool: True nếu lưu thành công
        
        Ví dụ:
            processor.save_image("output/result.jpg")
            processor.save_image()  # Tạo tên tự động
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để lưu")
            return False
        
        # Tạo đường dẫn nếu không cung cấp
        if output_path is None:
            output_path = utils.generate_output_filename()
        
        # Lưu ảnh
        return utils.save_image(self.processed_image, output_path)
    
    def display_image(self, title: str = "Image", wait_ms: int = 0) -> None:
        """
        Hiển thị ảnh trong cửa sổ.
        
        Args:
            title (str): Tiêu đề cửa sổ
            wait_ms (int): Thời gian chờ (ms). 0 = chờ nhấn phím bất kỳ
        
        Ví dụ:
            processor.display_image("Result", 1000)
            processor.display_image("Press any key to exit")
        """
        if self.processed_image is None:
            logger.warning("Không có ảnh để hiển thị")
            return
        
        try:
            # Tạo cửa sổ
            cv2.namedWindow(title, cv2.WINDOW_NORMAL)
            
            # Hiển thị ảnh
            cv2.imshow(title, self.processed_image)
            
            # Chờ
            key = cv2.waitKey(wait_ms)
            
            # Đóng cửa sổ
            cv2.destroyWindow(title)
            
            logger.debug(f"Hiển thị ảnh: {title}")
        
        except Exception as e:
            logger.error(f"✗ Lỗi hiển thị ảnh: {e}")
    
    def get_image_info(self) -> dict:
        """
        Lấy thông tin ảnh đã xử lý.
        
        Returns:
            dict: Thông tin ảnh
        
        Ví dụ:
            info = processor.get_image_info()
            print(f"Kích thước: {info['width']}x{info['height']}")
        """
        if self.processed_image is None:
            return {}
        
        return utils.get_image_info(self.processed_image)
    
    def print_image_info(self) -> None:
        """In thông tin ảnh ra console."""
        info = self.get_image_info()
        if not info:
            print("Không có ảnh")
            return
        
        print("=== Thông tin ảnh ===")
        print(f"Chiều rộng: {info['width']} px")
        print(f"Chiều cao: {info['height']} px")
        print(f"Channels: {info['channels']}")
        print(f"Data type: {info['dtype']}")
        print(f"Kích thước file: {info['size_mb']:.2f} MB")
        print(f"Aspect ratio: {info['aspect_ratio']:.2f}")
    
    def copy_image(self) -> Optional[np.ndarray]:
        """
        Tạo bản copy của ảnh đã xử lý.
        
        Returns:
            np.ndarray: Bản copy ảnh
        """
        if self.processed_image is None:
            return None
        return self.processed_image.copy()


if __name__ == "__main__":
    # Test ImageProcessor
    utils_logger = utils.setup_logging()
    
    try:
        # Khởi tạo processor
        processor = ImageProcessor()
        print("✓ ImageProcessor khởi tạo thành công")
        
        # Test tải ảnh
        test_image = "images/sample.jpg"
        if processor.load_image(test_image):
            # In thông tin
            processor.print_image_info()
            
            # Resize
            processor.resize_image(0.8)
            
            # Lưu
            if processor.save_image():
                print("✓ Lưu ảnh thành công")
        
        print("✓ Tất cả test hoàn tất!")
    
    except Exception as e:
        print(f"✗ Lỗi: {e}")
