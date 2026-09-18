from pathlib import Path
import json
import cv2

def save_intermediates(stages, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, image in stages.items():
        cv2.imwrite(str(output_dir / f"{name}.png"), image)

def save_json(report, output_path):
    Path(output_path).write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

def annotate_image(image, detections):
    result = image.copy()
    for i, item in enumerate(detections, start=1):
        b = item["features"]["bounding_box"]
        x, y, w, h = b["x"], b["y"], b["width"], b["height"]
        label = f'{i}: {item["shape"]}'
        cv2.rectangle(result, (x, y), (x+w, y+h), (255, 255, 255), 2)
        cv2.putText(
            result, label, (x, max(20, y-8)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2
        )
    return result

def save_annotated(image, detections, output_path):
    cv2.imwrite(str(output_path), annotate_image(image, detections))
