# -*- coding: utf-8 -*-
"""
Module phát hiện khuôn mặt (detector.py)
====================================
Lớp FaceDetector dùng Haar Cascade để nhận dạng và xử lý khuôn mặt trong ảnh.

Chức năng:
- Load Haar Cascade model
- Phát hiện khuôn mặt
- Vẽ khung nhận diện
- Tính toán thông tin khuôn mặt
- Áp dụng Non-Maximum Suppression

Tác giả: Trần Thành Nam
Phiên bản: 1.0
"""

import logging
from typing import List, Tuple, Optional
import numpy as np
import cv2

import config
import utils

logger = logging.getLogger(__name__)


class FaceDetector:
    """
    Lớp phát hiện khuôn mặt sử dụng Haar Cascade Classifier.
    
    Thuộc tính:
        face_cascade (cv2.CascadeClassifier): Mô hình Haar Cascade
        scale_factor (float): Scale factor cho detection
        min_neighbors (int): Minimum neighbors cho detection
        min_size (Tuple): Kích thước tối thiểu
        max_size (Tuple): Kích thước tối đa
        last_faces (List): Danh sách khuôn mặt từ frame trước
        detection_time (float): Thời gian detection (ms)
    
    Phương thức:
        detect_faces(): Phát hiện khuôn mặt trong ảnh
        draw_faces(): Vẽ khung khuôn mặt
        apply_nms(): Áp dụng Non-Maximum Suppression
        get_face_count(): Lấy số lượng khuôn mặt
        get_largest_face(): Lấy khuôn mặt lớn nhất
    """
    
    def __init__(self, cascade_path: str = config.CASCADE_PATH,
                 scale_factor: float = config.SCALE_FACTOR,
                 min_neighbors: int = config.MIN_NEIGHBORS,
                 min_size: Tuple[int, int] = config.MIN_FACE_SIZE,
                 max_size: Tuple[int, int] = config.MAX_FACE_SIZE):
        """
        Khởi tạo FaceDetector.
        
        Args:
            cascade_path (str): Đường dẫn file Haar Cascade
            scale_factor (float): Scale factor (1.05-1.3)
            min_neighbors (int): Minimum neighbors (4-6)
            min_size (Tuple): Kích thước tối thiểu khuôn mặt
            max_size (Tuple): Kích thước tối đa khuôn mặt
        
        Raises:
            ValueError: Nếu cascade file không tồn tại hoặc không hợp lệ
        """
        logger.info("Khởi tạo FaceDetector...")
        
        # Kiểm tra cascade file
        if not utils.is_valid_cascade(cascade_path):
            raise ValueError(f"Cascade file không hợp lệ: {cascade_path}")
        
        # Load cascade
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        logger.debug(f"✓ Load cascade từ: {cascade_path}")
        
        # Tham số detection
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.min_size = min_size
        self.max_size = max_size
        
        # Lưu trữ kết quả detection
        self.last_faces: List[Tuple[int, int, int, int]] = []
        self.detection_time = 0.0
        
        logger.info("✓ FaceDetector khởi tạo thành công")
    
    def detect_faces(self, image: np.ndarray, 
                     apply_nms: bool = True) -> List[Tuple[int, int, int, int]]:
        """
        Phát hiện khuôn mặt trong ảnh.
        
        Thuật toán:
        1. Convert ảnh sang grayscale nếu cần
        2. Gọi detectMultiScale() của Haar Cascade
        3. Lọc các khuôn mặt theo kích thước min/max
        4. Áp dụng NMS để loại bỏ overlap
        5. Sắp xếp theo diện tích (lớn đến bé)
        
        Args:
            image (np.ndarray): Ảnh input (BGR hoặc Grayscale)
            apply_nms (bool): Có áp dụng NMS hay không
        
        Returns:
            List[Tuple[int, int, int, int]]: Danh sách (x, y, width, height)
        
        Ví dụ:
            detector = FaceDetector()
            faces = detector.detect_faces(image)
            for (x, y, w, h) in faces:
                print(f"Khuôn mặt tại ({x}, {y}) - size: {w}x{h}")
        """
        import time
        
        if image is None or image.size == 0:
            logger.warning("Ảnh đầu vào trống")
            return []
        
        try:
            # Convert sang grayscale nếu cần
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image
            
            logger.debug(f"Ảnh grayscale: {gray.shape}")
            
            # Bắt đầu đo thời gian
            start_time = time.time()
            
            # Phát hiện khuôn mặt
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=self.scale_factor,
                minNeighbors=self.min_neighbors,
                flags=cv2.CASCADE_SCALE_IMAGE,
                minSize=self.min_size,
                maxSize=self.max_size
            )
            
            # Tính thời gian detection
            self.detection_time = (time.time() - start_time) * 1000  # ms
            
            logger.debug(f"Phát hiện {len(faces)} khuôn mặt (thời gian: {self.detection_time:.2f}ms)")
            
            # Convert tuple sang list
            faces_list = [(int(x), int(y), int(w), int(h)) 
                         for (x, y, w, h) in faces]
            
            # Áp dụng NMS nếu có overlap
            if apply_nms and len(faces_list) > 1:
                faces_list = self.apply_nms(faces_list)
                logger.debug(f"Sau NMS: {len(faces_list)} khuôn mặt")
            
            # Sắp xếp theo diện tích (lớn đến bé)
            faces_list.sort(key=lambda f: f[2] * f[3], reverse=True)
            
            # Lưu trữ kết quả
            self.last_faces = faces_list
            
            return faces_list
        
        except Exception as e:
            logger.error(f"✗ Lỗi phát hiện khuôn mặt: {e}")
            return []
    
    def apply_nms(self, faces: List[Tuple[int, int, int, int]], 
                  iou_threshold: float = config.IOU_THRESHOLD) -> List[Tuple[int, int, int, int]]:
        """
        Áp dụng Non-Maximum Suppression để loại bỏ overlap.
        
        NMS giữ lại các bounding box có IoU thấp, loại bỏ các overlap.
        
        Args:
            faces (List): Danh sách khuôn mặt (x, y, w, h)
            iou_threshold (float): Ngưỡng IoU (0.3 mặc định)
        
        Returns:
            List: Danh sách khuôn mặt sau NMS
        
        Ví dụ:
            faces = [(x1, y1, w1, h1), (x2, y2, w2, h2), ...]
            faces_nms = detector.apply_nms(faces, iou_threshold=0.3)
        """
        if len(faces) <= 1:
            return faces
        
        # Sắp xếp theo diện tích (lớn đến bé)
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        
        keep = []
        while len(faces) > 0:
            # Giữ lại box lớn nhất
            current = faces.pop(0)
            keep.append(current)
            
            # Loại bỏ các box overlap với box hiện tại
            remaining = []
            for face in faces:
                iou = utils.calculate_iou(current, face)
                if iou < iou_threshold:
                    remaining.append(face)
            
            faces = remaining
        
        logger.debug(f"NMS: {len(keep)} khuôn mặt được giữ lại")
        return keep
    
    def draw_faces(self, image: np.ndarray, 
                   faces: Optional[List[Tuple[int, int, int, int]]] = None,
                   face_color: Tuple[int, int, int] = config.FACE_COLOR,
                   text_color: Tuple[int, int, int] = config.TEXT_COLOR,
                   thickness: int = config.RECTANGLE_THICKNESS,
                   show_confidence: bool = True) -> np.ndarray:
        """
        Vẽ hình chữ nhật xung quanh khuôn mặt.
        
        Chức năng:
        - Vẽ khung chữ nhật (rect)
        - Vẽ số thứ tự khuôn mặt
        - Hiển thị tọa độ (tùy chọn)
        - Vẽ tổng số khuôn mặt
        
        Args:
            image (np.ndarray): Ảnh input
            faces (List): Danh sách khuôn mặt. Nếu None thì dùng last_faces
            face_color (Tuple): Màu khung (BGR)
            text_color (Tuple): Màu text (BGR)
            thickness (int): Độ dày đường vẽ
            show_confidence (bool): Có hiển thị độ tin cậy hay không
        
        Returns:
            np.ndarray: Ảnh sau khi vẽ
        
        Ví dụ:
            image = detector.draw_faces(image, faces)
            image = detector.draw_faces(image)  # Dùng last_faces
        """
        if image is None or image.size == 0:
            logger.warning("Ảnh đầu vào trống")
            return image
        
        # Dùng last_faces nếu không cung cấp
        if faces is None:
            faces = self.last_faces
        
        result_image = image.copy()
        
        # Vẽ từng khuôn mặt
        for idx, (x, y, w, h) in enumerate(faces, 1):
            try:
                # Vẽ khung chữ nhật
                cv2.rectangle(result_image, (x, y), (x + w, y + h),
                            face_color, thickness)
                
                # Vẽ số thứ tự và kích thước
                text = f"Face {idx}"
                if show_confidence:
                    text += f" {w}x{h}"
                
                # Vẽ text phía trên khung
                text_position = (x, y - 10)
                cv2.putText(result_image, text, text_position,
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                          text_color, 1, cv2.LINE_AA)
                
                # Vẽ tâm của khuôn mặt
                center = (x + w // 2, y + h // 2)
                cv2.circle(result_image, center, 3, text_color, -1)
            
            except Exception as e:
                logger.warning(f"Lỗi vẽ khuôn mặt {idx}: {e}")
                continue
        
        # Vẽ tổng số khuôn mặt phía dưới
        total_text = f"Total: {len(faces)} face(s)"
        cv2.putText(result_image, total_text, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                   text_color, 2, cv2.LINE_AA)
        
        logger.debug(f"Vẽ {len(faces)} khuôn mặt trên ảnh")
        
        return result_image
    
    def get_face_count(self) -> int:
        """
        Lấy số lượng khuôn mặt phát hiện được.
        
        Returns:
            int: Số lượng khuôn mặt
        """
        return len(self.last_faces)
    
    def get_largest_face(self) -> Optional[Tuple[int, int, int, int]]:
        """
        Lấy khuôn mặt lớn nhất.
        
        Returns:
            Tuple hoặc None: (x, y, width, height) hoặc None nếu không có
        """
        if len(self.last_faces) == 0:
            return None
        return self.last_faces[0]  # Đã được sắp xếp từ lớn đến bé
    
    def get_smallest_face(self) -> Optional[Tuple[int, int, int, int]]:
        """
        Lấy khuôn mặt nhỏ nhất.
        
        Returns:
            Tuple hoặc None: (x, y, width, height) hoặc None nếu không có
        """
        if len(self.last_faces) == 0:
            return None
        return self.last_faces[-1]  # Được sắp xếp từ lớn đến bé
    
    def get_detection_stats(self) -> dict:
        """
        Lấy thống kê detection.
        
        Returns:
            dict: Chứa face_count, detection_time, largest_face, etc.
        """
        stats = {
            'face_count': self.get_face_count(),
            'detection_time_ms': self.detection_time,
            'largest_face': self.get_largest_face(),
            'smallest_face': self.get_smallest_face(),
            'total_area': sum(w * h for (_, _, w, h) in self.last_faces)
        }
        return stats
    
    def reset(self) -> None:
        """Đặt lại detector."""
        self.last_faces = []
        self.detection_time = 0.0
        logger.debug("✓ Detector được đặt lại")


if __name__ == "__main__":
    # Test FaceDetector
    utils_logger = utils.setup_logging()
    
    try:
        # Khởi tạo detector
        detector = FaceDetector()
        print("✓ FaceDetector khởi tạo thành công")
        
        # Test load ảnh
        test_image_path = "images/sample.jpg"
        if utils.is_valid_image(test_image_path):
            image = cv2.imread(test_image_path)
            
            # Phát hiện khuôn mặt
            faces = detector.detect_faces(image)
            print(f"✓ Phát hiện {len(faces)} khuôn mặt")
            
            # Vẽ khuôn mặt
            result = detector.draw_faces(image, faces)
            
            # Lưu kết quả
            output_path = utils.generate_output_filename()
            if utils.save_image(result, output_path):
                print(f"✓ Lưu ảnh tại: {output_path}")
        
        print("✓ Tất cả test hoàn tất!")
    
    except Exception as e:
        print(f"✗ Lỗi: {e}")
