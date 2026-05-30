# -*- coding: utf-8 -*-
"""
Module quản lý webcam (camera.py)
====================================
Lớp CameraManager dùng để quản lý và xử lý video từ webcam.

Chức năng:
- Mở/đóng webcam
- Capture frame từ camera
- Lưu frame
- Lưu video
- Lấy thông tin camera (FPS, resolution)
- Điều chỉnh cài đặt camera

Tác giả: Trần Thành Nam
Phiên bản: 1.0
"""

import logging
from typing import Optional, Tuple
import numpy as np
import cv2

import config
import utils

logger = logging.getLogger(__name__)


class CameraManager:
    """
    Lớp quản lý webcam.
    
    Thuộc tính:
        camera_id (int): ID camera (0 = camera mặc định)
        camera (cv2.VideoCapture): Object VideoCapture
        is_opened (bool): Trạng thái camera
        fps (float): FPS của camera
        resolution (Tuple): Độ phân giải (width, height)
        frame_count (int): Số frame đã capture
        video_writer (cv2.VideoWriter): Writer cho video
    
    Phương thức:
        open_camera(): Mở camera
        close_camera(): Đóng camera
        capture_frame(): Capture một frame
        save_frame(): Lưu frame vào file ảnh
        save_video(): Lưu video
        get_properties(): Lấy thông tin camera
    """
    
    def __init__(self, camera_id: int = config.CAMERA_ID,
                 width: int = config.FRAME_WIDTH,
                 height: int = config.FRAME_HEIGHT):
        """
        Khởi tạo CameraManager.
        
        Args:
            camera_id (int): ID camera (0 = mặc định)
            width (int): Chiều rộng frame
            height (int): Chiều cao frame
        """
        logger.info("Khởi tạo CameraManager...")
        
        self.camera_id = camera_id
        self.camera: Optional[cv2.VideoCapture] = None
        self.is_opened = False
        self.fps = config.TARGET_FPS
        self.resolution = (width, height)
        self.frame_count = 0
        self.video_writer: Optional[cv2.VideoWriter] = None
        
        logger.info("✓ CameraManager khởi tạo thành công")
    
    def open_camera(self) -> bool:
        """
        Mở camera.
        
        Returns:
            bool: True nếu mở thành công, False nếu lỗi
        
        Ví dụ:
            camera = CameraManager()
            if camera.open_camera():
                print("✓ Camera đã được mở")
        """
        logger.info(f"Đang mở camera (ID: {self.camera_id})...")
        
        try:
            # Tạo VideoCapture object
            self.camera = cv2.VideoCapture(self.camera_id)
            
            # Kiểm tra camera mở thành công
            if not self.camera.isOpened():
                logger.error("✗ Không thể mở camera")
                return False
            
            # Cài đặt resolution
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
            
            # Cài đặt FPS
            self.camera.set(cv2.CAP_PROP_FPS, config.TARGET_FPS)
            
            # Cài đặt buffer
            self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            
            # Lấy thông tin thực tế
            actual_fps = self.camera.get(cv2.CAP_PROP_FPS)
            actual_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
            actual_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            self.fps = actual_fps
            self.resolution = (actual_width, actual_height)
            self.is_opened = True
            self.frame_count = 0
            
            logger.info(f"✓ Camera mở thành công")
            logger.debug(f"FPS: {self.fps}, Resolution: {self.resolution}")
            
            return True
        
        except Exception as e:
            logger.error(f"✗ Exception mở camera: {e}")
            self.is_opened = False
            return False
    
    def close_camera(self) -> bool:
        """
        Đóng camera và giải phóng tài nguyên.
        
        Returns:
            bool: True nếu đóng thành công
        
        Ví dụ:
            camera.close_camera()
        """
        logger.info("Đang đóng camera...")
        
        try:
            # Đóng video writer nếu có
            if self.video_writer is not None:
                self.video_writer.release()
                self.video_writer = None
            
            # Đóng camera
            if self.camera is not None:
                self.camera.release()
                self.camera = None
            
            self.is_opened = False
            logger.info(f"✓ Camera đóng thành công (Tổng frame: {self.frame_count})")
            
            return True
        
        except Exception as e:
            logger.error(f"✗ Exception đóng camera: {e}")
            return False
    
    def capture_frame(self) -> Optional[np.ndarray]:
        """
        Capture một frame từ camera.
        
        Returns:
            np.ndarray hoặc None: Frame ảnh (BGR), None nếu lỗi
        
        Ví dụ:
            frame = camera.capture_frame()
            if frame is not None:
                cv2.imshow("Frame", frame)
        """
        if not self.is_opened or self.camera is None:
            logger.warning("Camera chưa được mở")
            return None
        
        try:
            # Capture frame
            success, frame = self.camera.read()
            
            if not success or frame is None:
                logger.warning("Lỗi capture frame")
                return None
            
            # Cập nhật counter
            self.frame_count += 1
            
            return frame
        
        except Exception as e:
            logger.error(f"✗ Exception capture frame: {e}")
            return None
    
    def save_frame(self, output_path: Optional[str] = None) -> bool:
        """
        Lưu frame hiện tại vào file ảnh.
        
        Args:
            output_path (str): Đường dẫn output. Nếu None thì tạo tự động
        
        Returns:
            bool: True nếu lưu thành công
        
        Ví dụ:
            frame = camera.capture_frame()
            camera.save_frame("output/frame.jpg")
        """
        logger.info("Đang lưu frame...")
        
        # Capture frame hiện tại (lấy từ attribute cuối cùng)
        # Trong thực tế cần truyền frame vào, nhưng để đơn giản sẽ capture lại
        frame = self.capture_frame()
        
        if frame is None:
            logger.warning("Không thể capture frame để lưu")
            return False
        
        # Tạo đường dẫn nếu không cung cấp
        if output_path is None:
            output_path = utils.generate_output_filename("frame")
        
        # Lưu ảnh
        return utils.save_image(frame, output_path)
    
    def start_video_recording(self, output_path: Optional[str] = None,
                            codec: str = "MJPG") -> bool:
        """
        Bắt đầu ghi video.
        
        Args:
            output_path (str): Đường dẫn output video. Nếu None thì tạo tự động
            codec (str): Codec sử dụng (MJPG, XVID, mp4v, etc.)
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            camera.start_video_recording("output/video.avi")
        """
        if not self.is_opened or self.camera is None:
            logger.warning("Camera chưa được mở")
            return False
        
        # Tạo đường dẫn nếu không cung cấp
        if output_path is None:
            output_path = utils.generate_output_filename("video", ".avi")
        
        logger.info(f"Bắt đầu ghi video: {output_path}")
        
        try:
            # Tạo VideoWriter
            fourcc = cv2.VideoWriter_fourcc(*codec)
            
            self.video_writer = cv2.VideoWriter(
                output_path,
                fourcc,
                int(self.fps),
                self.resolution
            )
            
            if not self.video_writer.isOpened():
                logger.error("✗ Lỗi tạo VideoWriter")
                return False
            
            logger.info("✓ VideoWriter tạo thành công")
            return True
        
        except Exception as e:
            logger.error(f"✗ Exception tạo VideoWriter: {e}")
            return False
    
    def write_frame_to_video(self, frame: np.ndarray) -> bool:
        """
        Ghi frame vào video.
        
        Args:
            frame (np.ndarray): Frame cần ghi
        
        Returns:
            bool: True nếu ghi thành công
        
        Ví dụ:
            frame = camera.capture_frame()
            camera.write_frame_to_video(frame)
        """
        if self.video_writer is None:
            logger.warning("VideoWriter chưa được khởi tạo")
            return False
        
        if frame is None or frame.size == 0:
            logger.warning("Frame không hợp lệ")
            return False
        
        try:
            # Resize frame nếu cần
            if frame.shape[:2] != (self.resolution[1], self.resolution[0]):
                frame = utils.resize_to_resolution(
                    frame, self.resolution[0], self.resolution[1]
                )
            
            # Ghi frame
            self.video_writer.write(frame)
            return True
        
        except Exception as e:
            logger.error(f"✗ Exception ghi frame: {e}")
            return False
    
    def stop_video_recording(self) -> bool:
        """
        Dừng ghi video.
        
        Returns:
            bool: True nếu thành công
        
        Ví dụ:
            camera.stop_video_recording()
        """
        logger.info("Dừng ghi video...")
        
        if self.video_writer is None:
            logger.warning("VideoWriter chưa được khởi tạo")
            return False
        
        try:
            self.video_writer.release()
            self.video_writer = None
            logger.info("✓ Video recording dừng")
            return True
        
        except Exception as e:
            logger.error(f"✗ Exception dừng video: {e}")
            return False
    
    def get_frame_count(self) -> int:
        """
        Lấy số frame đã capture.
        
        Returns:
            int: Số frame
        """
        return self.frame_count
    
    def get_properties(self) -> dict:
        """
        Lấy thông tin camera.
        
        Returns:
            dict: Thông tin camera
        
        Ví dụ:
            props = camera.get_properties()
            print(f"FPS: {props['fps']}")
        """
        if not self.is_opened or self.camera is None:
            return {}
        
        try:
            properties = {
                'camera_id': self.camera_id,
                'is_opened': self.is_opened,
                'fps': self.fps,
                'width': self.resolution[0],
                'height': self.resolution[1],
                'resolution': self.resolution,
                'frame_count': self.frame_count,
                'brightness': self.camera.get(cv2.CAP_PROP_BRIGHTNESS),
                'contrast': self.camera.get(cv2.CAP_PROP_CONTRAST),
                'saturation': self.camera.get(cv2.CAP_PROP_SATURATION),
                'hue': self.camera.get(cv2.CAP_PROP_HUE),
                'exposure': self.camera.get(cv2.CAP_PROP_EXPOSURE)
            }
            return properties
        
        except Exception as e:
            logger.error(f"✗ Exception lấy properties: {e}")
            return {}
    
    def print_properties(self) -> None:
        """In thông tin camera ra console."""
        props = self.get_properties()
        if not props:
            print("Không có thông tin camera")
            return
        
        print("=== Thông tin Camera ===")
        print(f"Camera ID: {props['camera_id']}")
        print(f"Mở: {props['is_opened']}")
        print(f"FPS: {props['fps']:.1f}")
        print(f"Resolution: {props['width']}x{props['height']}")
        print(f"Frame count: {props['frame_count']}")
        print(f"Brightness: {props['brightness']:.1f}")
        print(f"Contrast: {props['contrast']:.1f}")
        print(f"Saturation: {props['saturation']:.1f}")
    
    def set_brightness(self, value: float) -> bool:
        """
        Cài đặt độ sáng camera.
        
        Args:
            value (float): Giá trị độ sáng (0-255)
        
        Returns:
            bool: True nếu thành công
        """
        if not self.is_opened or self.camera is None:
            return False
        
        try:
            self.camera.set(cv2.CAP_PROP_BRIGHTNESS, value)
            logger.debug(f"✓ Cài đặt brightness: {value}")
            return True
        except Exception as e:
            logger.error(f"✗ Exception cài đặt brightness: {e}")
            return False
    
    def set_contrast(self, value: float) -> bool:
        """
        Cài đặt độ tương phản.
        
        Args:
            value (float): Giá trị độ tương phản (0-255)
        
        Returns:
            bool: True nếu thành công
        """
        if not self.is_opened or self.camera is None:
            return False
        
        try:
            self.camera.set(cv2.CAP_PROP_CONTRAST, value)
            logger.debug(f"✓ Cài đặt contrast: {value}")
            return True
        except Exception as e:
            logger.error(f"✗ Exception cài đặt contrast: {e}")
            return False


if __name__ == "__main__":
    # Test CameraManager
    utils_logger = utils.setup_logging()
    
    try:
        # Khởi tạo camera
        camera = CameraManager()
        
        if camera.open_camera():
            # In thông tin
            camera.print_properties()
            
            # Capture vài frame
            for i in range(5):
                frame = camera.capture_frame()
                if frame is not None:
                    print(f"✓ Capture frame {i+1}: {frame.shape}")
            
            # Đóng camera
            camera.close_camera()
            print("✓ Tất cả test hoàn tất!")
        else:
            print("✗ Không thể mở camera")
    
    except Exception as e:
        print(f"✗ Lỗi: {e}")
