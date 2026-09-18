# VisionInspect: AI-Powered Computer Vision and Object Detection System

VisionInspect is a modular Python application combining classical Computer Vision and Machine Learning. It provides two complementary pipelines: OpenCV-based geometric shape analysis and YOLO-based real-world object detection.

## Features
- Image validation and preprocessing
- Contour detection and geometric feature extraction
- Rule-based shape classification for clean geometric images
- YOLO ML object detection for everyday photographs
- Multiple-object detection with confidence scores and bounding boxes
- JSON reports and annotated PNG outputs
- Intermediate preprocessing images
- Unit tests with pytest

## Technologies
Python, OpenCV, NumPy, Ultralytics YOLO, Pytest

## Installation
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On first ML detection, the selected YOLO weights may be downloaded automatically by Ultralytics. An internet connection is therefore required for the first model download.

## Run
Generate the CV sample:
```bash
python -m cvinspect.cli generate-sample --output data/sample_shapes.png
```
Analyze geometric shapes:
```bash
python -m cvinspect.cli analyze data/sample_shapes.png --output outputs --save-intermediate
```
Detect real-world objects in a normal photo:
```bash
python -m cvinspect.cli detect path/to/photo.jpg --output outputs
```
Optional confidence threshold:
```bash
python -m cvinspect.cli detect path/to/photo.jpg --confidence 0.50
```

## ML pipeline
Image → YOLO model → object localization → class prediction → confidence score → annotated image + JSON report.

## Testing
```bash
python -m pytest -q
```

## Limitations
The shape pipeline is intended for relatively clean geometric images. YOLO detection is limited to the classes learned by its pretrained model and can make incorrect predictions on unusual viewpoints, low-quality images, or objects outside its training vocabulary.

## Future enhancements
- Fine-tune YOLO on a domain-specific dataset
- Add a custom labelled dataset and confusion-matrix evaluation
- Add object tracking for video
- Add a GUI/web interface
- Add batch processing and performance benchmarking
