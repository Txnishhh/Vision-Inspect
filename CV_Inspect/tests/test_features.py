import numpy as np
import cv2
from cvinspect.features import contour_features

def test_square_features():
    contour = np.array([[[0,0]], [[100,0]], [[100,100]], [[0,100]]], dtype=np.int32)
    f = contour_features(contour, (200, 200, 3))
    assert f["area"] == 10000.0
    assert f["vertices"] == 4
    assert f["aspect_ratio"] == 1.0
