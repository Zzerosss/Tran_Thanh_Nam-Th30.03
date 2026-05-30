import pytest

import config
import utils
from detector import FaceDetector


def test_apply_nms_removes_overlapping_boxes():
    boxes = [
        (0, 0, 100, 100),
        (10, 10, 80, 80),
        (200, 200, 50, 50),
    ]

    detector = FaceDetector.__new__(FaceDetector)
    result = FaceDetector.apply_nms(detector, boxes, iou_threshold=0.3)

    assert len(result) == 2
    assert (200, 200, 50, 50) in result


def test_detect_faces_returns_list_if_cascade_available():
    if not utils.is_valid_cascade(config.CASCADE_PATH):
        pytest.skip("Haar cascade không khả dụng")

    detector = FaceDetector()
    assert detector.detect_faces is not None

    import numpy as np
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    faces = detector.detect_faces(image)
    assert isinstance(faces, list)


def test_draw_faces_draws_rectangles():
    detector = FaceDetector.__new__(FaceDetector)
    import numpy as np
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    faces = [(10, 10, 20, 20)]
    result = FaceDetector.draw_faces(detector, image.copy(), faces)
    assert result.shape == image.shape
