import pytest

def test_detector_module_imports():
    from cvinspect.object_detector import DEFAULT_MODEL
    assert DEFAULT_MODEL.endswith(".pt")

def test_detector_requires_valid_image():
    from cvinspect.object_detector import detect_objects
    import numpy as np
    with pytest.raises(ValueError):
        detect_objects(np.array([]))
