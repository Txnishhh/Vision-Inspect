import cv2
import numpy as np

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def denoise(gray):
    return cv2.GaussianBlur(gray, (5, 5), 0)

def adaptive_binary(blurred):
    return cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

def morphology(binary):
    kernel = np.ones((3, 3), np.uint8)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
    return cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=2)

def canny_edges(blurred):
    return cv2.Canny(blurred, 50, 150)

def preprocess(image):
    gray = to_grayscale(image)
    blurred = denoise(gray)
    binary = adaptive_binary(blurred)
    clean_mask = morphology(binary)
    edges = canny_edges(blurred)
    return {
        "gray": gray,
        "blurred": blurred,
        "binary": binary,
        "mask": clean_mask,
        "edges": edges,
    }
