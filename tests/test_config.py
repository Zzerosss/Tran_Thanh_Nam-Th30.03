from pathlib import Path
import config

def test_paths_exist():
    assert Path(config.BASE_DIR).exists()
    assert Path(config.IMAGES_DIR).exists()
    assert Path(config.OUTPUT_DIR).exists()
    assert Path(config.LOGS_DIR).exists()


def test_cascade_path_location():
    cascade_path = Path(config.CASCADE_PATH).resolve()
    assert cascade_path.parent == Path(config.BASE_DIR).resolve()
    assert cascade_path.suffix == ".xml"
