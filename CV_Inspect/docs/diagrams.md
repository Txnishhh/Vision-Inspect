# Design Diagrams

## Architecture
User/CLI → Image Validation → OpenCV Preprocessing → Shape Analysis → Result Reporter

In ML mode: User/CLI → Image Validation → YOLO Object Detector → Result Reporter → JSON + Annotated Image.

## Workflow
Input image → validation → selected pipeline → detection/classification → report generation → output image.

## Sequence
User → CLI → Image Loader → Detector/Analyzer → Reporter → Output Files.

## Component Diagram
Components: CLI, IO Utilities, Preprocessing, Segmentation, Feature Extraction, Shape Classifier, YOLO Object Detector, Reporter.

## Use Case
Actor: User. Use cases: provide image, run shape analysis, run ML object detection, inspect annotated result, inspect JSON report.

## ER Diagram
Not applicable. The application does not use persistent relational database storage.
