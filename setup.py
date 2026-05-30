# -*- coding: utf-8 -*-
"""
Script cài đặt dự án (setup.py)
====================================
Tải Haar Cascade, kiểm tra dependencies, cấu hình ban đầu.

Chạy: python setup.py
"""

import os
import sys
import urllib.request
from pathlib import Path

print("=" * 60)
print(" FACE DETECTION PROJECT - SETUP")
print("=" * 60)

# Thư mục gốc
BASE_DIR = Path(__file__).resolve().parent

print("\n📁 Kiểm tra cấu trúc thư mục...")

# Tạo thư mục cần thiết
directories = [
    BASE_DIR / "images",
    BASE_DIR / "output",
    BASE_DIR / "logs",
    BASE_DIR / ".vscode"
]

for directory in directories:
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Tạo: {directory.name}/")
    else:
        print(f"✓ Tồn tại: {directory.name}/")

print("\n📦 Kiểm tra thư viện Python...")

# Kiểm tra dependencies
required_packages = {
    'cv2': 'opencv-python',
    'numpy': 'numpy'
}

missing_packages = []

for package_name, pip_name in required_packages.items():
    try:
        __import__(package_name)
        print(f"✓ {pip_name} đã cài")
    except ImportError:
        print(f"✗ {pip_name} chưa cài")
        missing_packages.append(pip_name)

if missing_packages:
    print(f"\n⚠️  Cần cài: {', '.join(missing_packages)}")
    print("\nChạy lệnh:")
    print(f"  pip install {' '.join(missing_packages)}")
    sys.exit(1)

print("\n✓ Tất cả dependencies đã cài")

# Tải Haar Cascade
print("\n📥 Kiểm tra Haar Cascade...")

cascade_path = BASE_DIR / "haarcascade_frontalface_default.xml"

if cascade_path.exists():
    print(f"✓ {cascade_path.name} đã tồn tại")
else:
    print(f"⏳ Tải {cascade_path.name}...")
    
    url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    
    try:
        urllib.request.urlretrieve(url, str(cascade_path))
        print(f"✓ Tải thành công: {cascade_path.name}")
    except Exception as e:
        print(f"✗ Lỗi tải: {e}")
        print("\n📌 Hướng dẫn thủ công:")
        print(f"1. Vào: {url}")
        print(f"2. Lưu file vào: {cascade_path}")
        sys.exit(1)

# Tạo VS Code config
print("\n⚙️  Cấu hình VS Code...")

vscode_dir = BASE_DIR / ".vscode"

# launch.json
launch_json = vscode_dir / "launch.json"
launch_config = """{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Face Detection",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}"""

if not launch_json.exists():
    with open(launch_json, 'w') as f:
        f.write(launch_config)
    print(f"✓ Tạo: .vscode/launch.json")
else:
    print(f"✓ Tồn tại: .vscode/launch.json")

# settings.json
settings_json = vscode_dir / "settings.json"
settings_config = """{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "autopep8",
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}"""

if not settings_json.exists():
    with open(settings_json, 'w') as f:
        f.write(settings_config)
    print(f"✓ Tạo: .vscode/settings.json")
else:
    print(f"✓ Tồn tại: .vscode/settings.json")

# Test imports
print("\n🧪 Kiểm tra imports...")

try:
    import cv2
    import numpy as np
    print(f"✓ OpenCV {cv2.__version__}")
    print(f"✓ NumPy {np.__version__}")
except ImportError as e:
    print(f"✗ Lỗi import: {e}")
    sys.exit(1)

# Hoàn tất
print("\n" + "=" * 60)
print("✅ CÀI ĐẶT HOÀN TẤT!")
print("=" * 60)
print("\n📝 Tiếp theo:")
print("1. Thêm ảnh vào thư mục 'images/'")
print("2. Chạy: python main.py")
print("\n🎉 Chúc bạn sử dụng vui vẻ!\n")
