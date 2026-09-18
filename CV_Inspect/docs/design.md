# Design Decisions & Rationale

## Architecture
A modular pipeline architecture was selected because each computer vision stage has a clear responsibility. This makes the code easier to test, replace, and extend.

## Why OpenCV?
OpenCV provides mature implementations of image conversion, filtering, thresholding, morphology, Canny edge detection, contour extraction, moments, and geometric measurements.

## Why Rule-Based Classification?
The project is designed to demonstrate fundamental computer vision concepts without requiring model downloads, GPU hardware, a dataset, or an internet connection. Shape classification is therefore based on contour geometry.

## Input/Output
Input: one local image path.

Outputs:
- annotated PNG
- JSON report
- optional intermediate processing images

## Error Handling
- Missing files raise `FileNotFoundError`.
- Unsupported extensions raise `ValueError`.
- Undecodable images raise `ValueError`.
- CLI arguments are validated by `argparse`.

## Non-Functional Requirements
1. Performance: analyze normal classroom-sized images within a few seconds on a typical laptop.
2. Usability: provide clear commands, help text, and readable terminal output.
3. Reliability: validate input and avoid silently processing invalid files.
4. Maintainability: separate I/O, preprocessing, segmentation, features, classification, analysis, and reporting.
5. Scalability: stages can be replaced with ML detectors or batch processing later.
6. Resource efficiency: processing is local and does not require a server or database.
7. Testability: core feature and classifier functions have automated tests.
8. Portability: Python/OpenCV implementation works across Windows, Linux, and macOS with Python support.
