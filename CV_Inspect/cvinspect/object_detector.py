from pathlib import Path
import cv2

try:
    from ultralytics import YOLO
except ImportError as exc:
    YOLO = None
    _IMPORT_ERROR = exc

DEFAULT_MODEL = "yolo11n.pt"

def detect_objects(image, model_path=DEFAULT_MODEL, confidence=0.35):
    """Run YOLO object detection and return JSON-friendly detections + annotated image."""
    if YOLO is None:
        raise RuntimeError("Ultralytics is not installed. Run: python -m pip install -r requirements.txt") from _IMPORT_ERROR
    if image is None or image.size == 0:
        raise ValueError("Invalid image supplied to object detector")

    model = YOLO(model_path)
    results = model.predict(source=image, conf=confidence, verbose=False)
    result = results[0]
    names = result.names
    detections = []

    if result.boxes is not None:
        for box in result.boxes:
            xyxy = box.xyxy[0].tolist()
            cls_id = int(box.cls[0].item())
            score = float(box.conf[0].item())
            x1, y1, x2, y2 = [int(round(v)) for v in xyxy]
            detections.append({
                "class": str(names[cls_id]),
                "confidence": round(score, 4),
                "bounding_box": {"x": x1, "y": y1, "width": max(0, x2-x1), "height": max(0, y2-y1)},
            })

    annotated = result.plot()
    summary = {}
    for d in detections:
        summary[d["class"]] = summary.get(d["class"], 0) + 1

    return {"model": model_path, "confidence_threshold": confidence, "objects_detected": len(detections), "class_summary": summary, "detections": detections}, annotated
