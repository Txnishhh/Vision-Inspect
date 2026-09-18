from pathlib import Path
import cv2

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

def validate_image_path(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Image not found: {p}")
    if p.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported image format: {p.suffix}")
    return p

def load_image(path: str):
    p = validate_image_path(path)
    image = cv2.imread(str(p))
    if image is None:
        raise ValueError(f"OpenCV could not decode image: {p}")
    return image
