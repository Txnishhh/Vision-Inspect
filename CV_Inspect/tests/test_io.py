import pytest
from cvinspect.io_utils import validate_image_path

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        validate_image_path("does_not_exist.png")

def test_bad_extension(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("not an image")
    with pytest.raises(ValueError):
        validate_image_path(str(p))
