# -*- coding: utf-8 -*-
"""
File chính ứng dụng (main.py)
====================================
Điểm vào chính của ứng dụng nhận dạng khuôn mặt.

Chức năng:
- Hiển thị menu chính
- Quản lý các mode (ảnh tĩnh, webcam)
- Xử lý input người dùng
- Tích hợp detector, image processor, camera manager
- Xử lý lỗi toàn diện

Tác giả: Trần Thành Nam
Phiên bản: 1.0
"""

import logging
import os
import sys
from pathlib import Path
import cv2
import numpy as np

import config
import utils
from detector import FaceDetector
from image_processor import ImageProcessor
from camera import CameraManager

# Setup logging
logger = utils.setup_logging()
logger.info("=" * 50)
logger.info(f"Khởi động {config.APP_NAME} v{config.APP_VERSION}")
logger.info("=" * 50)


class Application:
    """
    Lớp ứng dụng chính.
    
    Chức năng:
    - Quản lý menu
    - Xử lý mode ảnh tĩnh
    - Xử lý mode webcam
    - Tích hợp các module
    
    Thuộc tính:
        detector (FaceDetector): Bộ phát hiện khuôn mặt
        image_processor (ImageProcessor): Xử lý ảnh
        camera (CameraManager): Quản lý camera
        fps_counter (FPSCounter): Đếm FPS
    """
    
    def __init__(self):
        """Khởi tạo ứng dụng."""
        logger.info("Khởi tạo ứng dụng...")
        
        try:
            # Khởi tạo detector
            self.detector = FaceDetector()
            logger.info("✓ Detector khởi tạo")
            
            # Khởi tạo image processor
            self.image_processor = ImageProcessor()
            logger.info("✓ Image processor khởi tạo")
            
            # Khởi tạo camera manager
            self.camera = CameraManager()
            logger.info("✓ Camera manager khởi tạo")
            
            # FPS counter
            self.fps_counter = utils.FPSCounter()
            
            logger.info("✓ Ứng dụng khởi tạo thành công")
        
        except Exception as e:
            logger.error(f"✗ Lỗi khởi tạo: {e}")
            raise
    
    def show_menu(self) -> int:
        """
        Hiển thị menu chính.
        
        Returns:
            int: Lựa chọn menu
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "=" * 50)
        print(f"  {config.APP_NAME} v{config.APP_VERSION}")
        print("=" * 50)
        print("\n┌─ MENU CHÍNH ──────────────────────────────┐")
        print("│                                           │")
        print("│  [1] Phát hiện khuôn mặt từ ảnh tĩnh     │")
        print("│  [2] Phát hiện khuôn mặt từ webcam       │")
        print("│  [0] Thoát chương trình                  │")
        print("│                                           │")
        print("└───────────────────────────────────────────┘\n")
        
        try:
            choice = int(input("Chọn lựa chọn (0-2): "))
            return choice
        except ValueError:
            logger.warning("Lựa chọn không hợp lệ")
            return -1

    def select_image_path(self) -> str:
        """
        Chọn ảnh để xử lý trong mode ảnh tĩnh.
        """
        print("\n┌─ MODE ẢNH TĨNH ────────────────────────────┐")
        print("│ Nhập đường dẫn ảnh hoặc để trống để chọn   │")
        print("│ từ thư mục 'images'                        │")
        print("│ Nhập Q để quay lại menu                    │")
        print("└────────────────────────────────────────────┘\n")

        image_path = input("Đường dẫn ảnh: ").strip()
        if image_path.lower() == 'q':
            return ""

        if not image_path:
            if not os.path.exists(config.IMAGES_DIR):
                print("✗ Thư mục 'images' không tồn tại")
                logger.warning("Thư mục images không tồn tại")
                return ""

            images = [f for f in os.listdir(config.IMAGES_DIR)
                      if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
            images.sort()

            if not images:
                print("✗ Không có ảnh trong thư mục 'images'")
                logger.warning("Không có ảnh trong thư mục images")
                return ""

            for idx, img in enumerate(images, 1):
                print(f"  {idx}. {img}")

            choice = input(f"\nChọn ảnh (1-{len(images)}): ").strip()
            if not choice.isdigit():
                print("✗ Lựa chọn không hợp lệ")
                return ""

            index = int(choice) - 1
            if index < 0 or index >= len(images):
                print("✗ Lựa chọn không hợp lệ")
                return ""

            return str(Path(config.IMAGES_DIR) / images[index])

        candidate = Path(image_path)
        if candidate.is_file():
            return str(candidate)

        candidate = Path(config.IMAGES_DIR) / image_path
        if candidate.is_file():
            return str(candidate)

        candidate = Path.cwd() / image_path
        if candidate.is_file():
            return str(candidate)

        print("✗ Ảnh không tìm thấy")
        logger.error(f"Ảnh không tìm thấy: {image_path}")
        return ""

    def run_image_mode(self) -> None:
        """
        Xử lý mode ảnh tĩnh.
        
        Chức năng:
        - Yêu cầu chọn ảnh
        - Load ảnh
        - Phát hiện khuôn mặt
        - Vẽ khuôn mặt
        - Hiển thị kết quả
        - Lưu ảnh
        """
        logger.info("=" * 50)
        logger.info("MỘT TRONG CÁC ÔN IMAGE MODE")
        logger.info("=" * 50)

        image_path = self.select_image_path()
        if not image_path:
            return

        print(f"\nĐang load ảnh: {image_path}")
        if not self.image_processor.load_image(image_path):
            print("✗ Lỗi load ảnh")
            return

        print("✓ Load ảnh thành công")

        print("Đang phát hiện khuôn mặt...")
        image = self.image_processor.get_processed_image()
        faces = self.detector.detect_faces(image)
        print(f"✓ Phát hiện: {len(faces)} khuôn mặt")

        result_image = self.detector.draw_faces(image, faces)

        save_answer = input("\nCó lưu ảnh không? (y/n): ").strip().lower()
        if save_answer == 'y':
            output_path = utils.generate_output_filename()
            if utils.save_image(result_image, output_path):
                print(f"✓ Lưu ảnh: {output_path}")
                logger.info(f"✓ Lưu ảnh: {output_path}")

        print("\nHiển thị ảnh (Nhấn bất kỳ phím nào để tiếp tục)")
        cv2.namedWindow("Face Detection Result", cv2.WINDOW_NORMAL)
        cv2.imshow("Face Detection Result", result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        logger.info("✓ Mode ảnh tĩnh hoàn tất")
    
    def run_camera_mode(self) -> None:
        """
        Xử lý mode webcam.
        
        Chức năng:
        - Mở camera
        - Loop capture frame
        - Phát hiện khuôn mặt trên từng frame
        - Hiển thị real-time
        - Xử lý các phím tắt
        - Thoát an toàn
        
        Phím tắt:
        - 'q': Thoát
        - 's': Lưu frame
        - 'v': Ghi video (bắt đầu/dừng)
        - 'p': Pause
        - ESC: Thoát
        """
        logger.info("=" * 50)
        logger.info("MỘT TRONG CÁC ÔN CAMERA MODE")
        logger.info("=" * 50)
        
        print("\n┌─ MODE WEBCAM ──────────────────────────────┐")
        print("│ Phím tắt:                                  │")
        print("│  Q: Thoát                                  │")
        print("│  S: Lưu frame                              │")
        print("│  V: Ghi video (bắt đầu/dừng)              │")
        print("│  P: Tạm dừng                               │")
        print("│ ESC: Thoát                                 │")
        print("└────────────────────────────────────────────┘\n")
        
        # Mở camera
        print("Đang mở camera...")
        if not self.camera.open_camera():
            print("✗ Lỗi mở camera")
            logger.error("✗ Lỗi mở camera")
            return
        
        print("✓ Camera đã được mở")
        self.camera.print_properties()
        
        # Khởi tạo
        recording = False
        paused = False
        self.fps_counter.reset()
        
        print("\nBắt đầu xử lý... (Nhấn Q để thoát)")
        
        try:
            while True:
                # Capture frame
                frame = self.camera.capture_frame()
                
                if frame is None:
                    break
                
                # Copy frame để vẽ
                if not paused:
                    display_frame = frame.copy()
                    
                    # Phát hiện khuôn mặt
                    faces = self.detector.detect_faces(display_frame)
                    
                    # Vẽ khuôn mặt
                    display_frame = self.detector.draw_faces(display_frame, faces)
                    
                    # Tính FPS
                    self.fps_counter.update()
                    fps = self.fps_counter.get_fps()
                    
                    # Vẽ FPS
                    fps_text = f"FPS: {fps:.1f} | Faces: {len(faces)}"
                    cv2.putText(display_frame, fps_text, (10, 60),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                              config.TEXT_COLOR, 2)
                    
                    # Ghi video nếu đang ghi
                    if recording:
                        self.camera.write_frame_to_video(display_frame)
                        cv2.putText(display_frame, "REC", (10, 90),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                  (0, 0, 255), 2)
                    
                    # Hiển thị
                    cv2.imshow("Face Detection - Webcam", display_frame)
                
                # Xử lý phím
                key = cv2.waitKey(1) & 0xFF
                
                # Thoát
                if key == ord('q') or key == ord('Q') or key == 27:  # ESC
                    print("\n✓ Thoát chương trình")
                    break
                
                # Lưu frame
                elif key == ord('s') or key == ord('S'):
                    frame_path = utils.generate_output_filename("frame")
                    if utils.save_image(frame, frame_path):
                        print(f"✓ Frame đã lưu: {frame_path}")
                        logger.info(f"✓ Frame đã lưu: {frame_path}")
                
                # Bắt đầu/dừng ghi video
                elif key == ord('v') or key == ord('V'):
                    if not recording:
                        video_path = utils.generate_output_filename("video", ".avi")
                        if self.camera.start_video_recording(video_path):
                            recording = True
                            print(f"✓ Bắt đầu ghi video: {video_path}")
                            logger.info(f"✓ Bắt đầu ghi video: {video_path}")
                    else:
                        if self.camera.stop_video_recording():
                            recording = False
                            print("✓ Dừng ghi video")
                            logger.info("✓ Dừng ghi video")
                
                # Pause/Resume
                elif key == ord('p') or key == ord('P'):
                    paused = not paused
                    status = "Tạm dừng" if paused else "Tiếp tục"
                    print(f"✓ {status}")
                    logger.info(f"✓ {status}")
        
        except KeyboardInterrupt:
            print("\n✓ Interrupt - Thoát chương trình")
            logger.info("✓ Interrupt - Thoát")
        
        except Exception as e:
            logger.error(f"✗ Exception trong camera mode: {e}")
            print(f"✗ Lỗi: {e}")
        
        finally:
            # Cleanup
            if recording:
                self.camera.stop_video_recording()
            
            self.camera.close_camera()
            cv2.destroyAllWindows()
            
            print(f"\n✓ Xử lý {self.camera.get_frame_count()} frame")
            logger.info(f"✓ Camera mode hoàn tất ({self.camera.get_frame_count()} frames)")
    
    def run(self) -> None:
        """
        Chạy ứng dụng chính.
        
        Vòng lặp chính:
        1. Hiển thị menu
        2. Lấy lựa chọn
        3. Xử lý lựa chọn
        4. Lặp lại hoặc thoát
        """
        logger.info("Vào vòng lặp chính")
        
        while True:
            choice = self.show_menu()
            
            if choice == 1:
                # Mode ảnh tĩnh
                try:
                    self.run_image_mode()
                except Exception as e:
                    logger.error(f"✗ Lỗi image mode: {e}")
                    print(f"✗ Lỗi: {e}")
            
            elif choice == 2:
                # Mode camera
                try:
                    self.run_camera_mode()
                except Exception as e:
                    logger.error(f"✗ Lỗi camera mode: {e}")
                    print(f"✗ Lỗi: {e}")
            
            elif choice == 0:
                # Thoát
                print("\nCảm ơn đã sử dụng ứng dụng!")
                logger.info("=" * 50)
                logger.info("✓ Thoát ứng dụng")
                logger.info("=" * 50)
                break
            
            else:
                print("✗ Lựa chọn không hợp lệ")
                logger.warning(f"Lựa chọn không hợp lệ: {choice}")
            
            # Pause trước khi quay lại menu
            if choice != 0:
                input("\nNhấn Enter để tiếp tục...")


def main():
    """
    Hàm main.
    
    Xử lý:
    - Khởi tạo ứng dụng
    - Chạy vòng lặp chính
    - Xử lý lỗi toàn cục
    - Cleanup
    """
    app = None
    
    try:
        # Khởi tạo ứng dụng
        app = Application()
        
        # Chạy
        app.run()
    
    except Exception as e:
        logger.critical(f"✗ Lỗi crítico: {e}", exc_info=True)
        print(f"✗ Lỗi Critical: {e}")
        sys.exit(1)
    
    finally:
        # Cleanup
        cv2.destroyAllWindows()
        logger.info("✓ Ứng dụng đã thoát an toàn")


if __name__ == "__main__":
    main()
