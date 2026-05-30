import tempfile
from pathlib import Path

import cv2
import numpy as np
import pytest

import config
import utils


def test_generate_output_filename():
    path = utils.generate_output_filename("test", ".png")
    assert path.endswith(".png")
    assert "test_" in Path(path).name
    assert Path(path).parent == Path(config.OUTPUT_DIR)


def test_calculate_iou_non_overlap():
    assert utils.calculate_iou((0, 0, 10, 10), (20, 20, 10, 10)) == 0.0


def test_calculate_iou_partial_overlap():
    iou = utils.calculate_iou((0, 0, 10, 10), (5, 5, 10, 10))
    assert 0.0 < iou < 1.0


def test_get_image_info():
    image = np.zeros((20, 40, 3), dtype=np.uint8)
    info = utils.get_image_info(image)
    assert info["width"] == 40
    assert info["height"] == 20
    assert info["channels"] == 3
    assert info["dtype"] == "uint8"
    assert info["size_bytes"] == image.nbytes


def test_color_conversion_roundtrip():
    image = np.zeros((2, 2, 3), dtype=np.uint8)
    image[0, 0] = (255, 0, 0)

    rgb = utils.bgr_to_rgb(image)
    assert tuple(rgb[0, 0]) == (0, 0, 255)

    bgr = utils.rgb_to_bgr(rgb)
    assert tuple(bgr[0, 0]) == (255, 0, 0)
    assert np.array_equal(image, bgr)


def test_resize_image_invalid_scale():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    resized = utils.resize_image(image, scale=-1)
    assert resized.shape == (5, 5, 3)


def test_save_image_and_is_valid_image():
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "tmp_test.jpg"
        assert utils.save_image(image, str(output_path))
        assert utils.file_exists(str(output_path))
        assert utils.is_valid_image(str(output_path))
        assert not utils.is_valid_image(str(output_path.with_suffix('.txt')))


def test_is_valid_cascade_invalid_path():
    assert not utils.is_valid_cascade("/path/does/not/exist.xml")


def test_fps_counter():
    counter = utils.FPSCounter(average_count=5)
    assert counter.get_fps() == 0.0
    counter.update()
    counter.update()
    assert isinstance(counter.get_fps(), float)
    counter.reset()
    assert counter.get_fps() == 0.0
