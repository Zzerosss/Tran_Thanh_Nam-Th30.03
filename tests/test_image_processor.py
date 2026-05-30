import tempfile
from pathlib import Path

import cv2
import numpy as np

from image_processor import ImageProcessor
import utils


def create_temp_image(path: Path) -> None:
    image = np.full((20, 30, 3), 255, dtype=np.uint8)
    cv2.imwrite(str(path), image)


def test_load_image_and_transformations():
    with tempfile.TemporaryDirectory() as tmpdir:
        image_path = Path(tmpdir) / "sample.jpg"
        create_temp_image(image_path)

        processor = ImageProcessor()
        assert processor.load_image(str(image_path))
        assert processor.get_original_image() is not None
        assert processor.get_processed_image() is not None

        assert processor.resize_image(0.5)
        assert processor.get_processed_image().shape[:2] == (10, 15)

        assert processor.reset_to_original()
        assert processor.get_processed_image().shape[:2] == (20, 30)

        assert processor.convert_to_grayscale()
        assert processor.get_processed_image().ndim == 2

        assert processor.resize_to_resolution(10, 10)
        assert processor.get_processed_image().shape == (10, 10)


def test_load_image_invalid_file():
    processor = ImageProcessor()
    assert not processor.load_image("nonexistent_file.png")
