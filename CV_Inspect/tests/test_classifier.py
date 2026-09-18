from cvinspect.classifier import classify_shape

def test_triangle():
    assert classify_shape({
        "vertices": 3, "circularity": 0.4, "aspect_ratio": 1.0, "extent": 0.5
    }) == "triangle"

def test_square():
    assert classify_shape({
        "vertices": 4, "circularity": 0.7, "aspect_ratio": 1.0, "extent": 0.8
    }) == "square"

def test_rectangle():
    assert classify_shape({
        "vertices": 4, "circularity": 0.7, "aspect_ratio": 2.0, "extent": 0.8
    }) == "rectangle"

def test_circle():
    assert classify_shape({
        "vertices": 12, "circularity": 0.9, "aspect_ratio": 1.0, "extent": 0.78
    }) == "circle"
