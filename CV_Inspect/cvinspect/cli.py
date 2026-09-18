import argparse
from pathlib import Path
import cv2
import numpy as np

from .io_utils import load_image
from .analyzer import analyze_image
from .object_detector import detect_objects
from .reporter import save_intermediates, save_json, save_annotated

def generate_sample(path):
    canvas = np.ones((600, 900, 3), dtype=np.uint8) * 255
    cv2.circle(canvas, (170, 170), 90, (0, 0, 0), -1)
    cv2.rectangle(canvas, (330, 90), (520, 270), (0, 0, 0), -1)
    cv2.rectangle(canvas, (600, 100), (830, 250), (0, 0, 0), -1)
    triangle = np.array([[180, 430], [80, 560], [280, 560]], dtype=np.int32)
    cv2.fillPoly(canvas, [triangle], (0, 0, 0))
    cv2.circle(canvas, (500, 470), 70, (0, 0, 0), -1)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), canvas)

def analyze_command(args):
    image = load_image(args.input)
    report, stages = analyze_image(image, min_area=args.min_area)
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    save_json(report, out / "analysis.json")
    save_annotated(image, report["detections"], out / "annotated.png")
    if args.save_intermediate: save_intermediates(stages, out)
    print("=" * 55); print("CV-INSPECT SHAPE ANALYSIS"); print("=" * 55)
    print(f"Image size       : {report['image']['width']} x {report['image']['height']}")
    print(f"Objects detected : {report['objects_detected']}")
    print(f"Shape summary    : {report['shape_summary']}")
    print(f"JSON report      : {out / 'analysis.json'}")
    print(f"Annotated image  : {out / 'annotated.png'}")

def detect_command(args):
    image = load_image(args.input)
    report, annotated = detect_objects(image, model_path=args.model, confidence=args.confidence)
    out = Path(args.output); out.mkdir(parents=True, exist_ok=True)
    report["image"] = {"width": int(image.shape[1]), "height": int(image.shape[0]), "channels": int(image.shape[2]) if len(image.shape)==3 else 1}
    save_json(report, out / "ml_detection.json")
    cv2.imwrite(str(out / "ml_annotated.png"), annotated)
    print("=" * 55); print("VISIONINSPECT ML OBJECT DETECTION"); print("=" * 55)
    print(f"Model            : {report['model']}")
    print(f"Objects detected : {report['objects_detected']}")
    print(f"Class summary    : {report['class_summary']}")
    print(f"JSON report      : {out / 'ml_detection.json'}")
    print(f"Annotated image  : {out / 'ml_annotated.png'}")
    print("=" * 55)

def main():
    parser = argparse.ArgumentParser(prog="cvinspect", description="Computer vision and ML image analysis system.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("analyze", help="Analyze geometric shapes with OpenCV.")
    p.add_argument("input"); p.add_argument("--output", default="outputs"); p.add_argument("--min-area", type=int, default=300); p.add_argument("--save-intermediate", action="store_true"); p.set_defaults(func=analyze_command)
    p = sub.add_parser("detect", help="Detect real-world objects using a YOLO ML model.")
    p.add_argument("input", help="Path to JPG/PNG/BMP/TIFF image"); p.add_argument("--output", default="outputs"); p.add_argument("--model", default="yolo11n.pt", help="YOLO model weights; downloaded automatically on first use"); p.add_argument("--confidence", type=float, default=0.35); p.set_defaults(func=detect_command)
    p = sub.add_parser("generate-sample", help="Generate a synthetic shape image.")
    p.add_argument("--output", default="data/sample_shapes.png"); p.set_defaults(func=lambda a: generate_sample(a.output))
    args=parser.parse_args(); args.func(args)

if __name__ == "__main__": main()
