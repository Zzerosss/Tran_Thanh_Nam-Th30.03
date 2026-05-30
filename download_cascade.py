#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tải Haar Cascade
====================================
Tải file haarcascade_frontalface_default.xml từ OpenCV GitHub
"""

import urllib.request
import os
from pathlib import Path

def download_cascade():
    """Tải file Haar Cascade"""
    
    print("⏳ Đang tải Haar Cascade...")
    
    base_dir = Path(__file__).resolve().parent
    cascade_path = base_dir / "haarcascade_frontalface_default.xml"
    
    # URL từ OpenCV repository
    url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    
    try:
        print(f"Nguồn: {url}")
        print(f"Đích: {cascade_path}")
        
        # Tải file
        urllib.request.urlretrieve(url, str(cascade_path))
        
        # Kiểm tra file size
        size = os.path.getsize(cascade_path) / 1024  # KB
        
        print(f"\n✅ Tải thành công!")
        print(f"File size: {size:.1f} KB")
        print(f"Vị trí: {cascade_path}")
        
        return True
    
    except Exception as e:
        print(f"\n❌ Lỗi tải: {e}")
        print(f"\nHướng dẫn thủ công:")
        print(f"1. Vào: {url}")
        print(f"2. Lưu file vào: {cascade_path}")
        return False

if __name__ == "__main__":
    success = download_cascade()
    exit(0 if success else 1)
