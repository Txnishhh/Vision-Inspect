# VisionInspect --- Automated Shape Detection and Image Analysis

## Overview

VisionInspect is a Python-based computer vision project that
automatically analyzes images to detect and classify geometric shapes.
The system follows a modular computer vision pipeline consisting of
image input, preprocessing, segmentation, feature extraction,
classification, analysis, and result reporting.

The project is designed to reduce the time and inconsistency associated
with manual shape inspection while providing structured and annotated
results.

## Features

-   Image input and validation
-   Image preprocessing and noise reduction
-   Object and shape detection using contours
-   Geometric feature extraction
-   Rule-based shape classification
-   Result generation
-   Annotated image generation
-   Command-Line Interface (CLI)
-   JSON-based output
-   Modular architecture
-   Automated testing

## Technologies / Tools Used

-   **Python** --- Core programming language
-   **OpenCV** --- Image processing, segmentation, and contour detection
-   **NumPy** --- Numerical and array operations
-   **JSON** --- Structured result output
-   **Git/GitHub** --- Version control and project management
-   **pytest** --- Testing

## Project Structure

``` text
VisionInspect/
├── io_utils.py
├── preprocessing.py
├── segmentation.py
├── features.py
├── classifier.py
├── analyzer.py
├── reporter.py
├── cli.py
├── tests/
└── README.md
```

### Module Description

-   `io_utils.py` --- Handles image loading, validation, and file
    operations.
-   `preprocessing.py` --- Performs image preparation such as grayscale
    conversion, resizing, filtering, and noise reduction.
-   `segmentation.py` --- Separates objects from the background and
    detects contours.
-   `features.py` --- Extracts geometric features such as area,
    perimeter, aspect ratio, circularity, and vertices.
-   `classifier.py` --- Classifies detected objects into geometric shape
    categories.
-   `analyzer.py` --- Coordinates the complete image-analysis pipeline.
-   `reporter.py` --- Produces analysis results and annotated output
    images.
-   `cli.py` --- Provides the command-line interface for running the
    system.

## Installation

### 1. Clone the repository

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd VisionInspect
```

### 2. Create a virtual environment

**Windows:**

``` bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install opencv-python numpy pytest
```

If the project contains a requirements file, use:

``` bash
pip install -r requirements.txt
```

## Running the Project

Run the CLI using:

``` bash
python cli.py <path_to_image>
```

Replace `<path_to_image>` with the location of the image you want to
analyze.

Example:

``` bash
python cli.py samples/shapes.jpg
```

The system will validate the image, preprocess it, detect contours,
extract geometric features, classify the shapes, and generate the final
results.

## Testing

The project uses automated tests to verify individual components and the
complete analysis pipeline.

Run all tests with:

``` bash
pytest
```

### Current Test Result

**9 tests passed successfully.**

The testing approach covers:

-   Unit testing
-   Image input validation
-   Feature extraction
-   Shape classification
-   Overall evaluation

## Output

VisionInspect can produce:

-   Detected shape information
-   Extracted geometric features
-   Classification results
-   Structured JSON output
-   Annotated images showing detected contours and labels

## Computer Vision Pipeline

``` text
Input Image
     ↓
Image Validation
     ↓
Preprocessing
     ↓
Segmentation / Contour Detection
     ↓
Feature Extraction
     ↓
Shape Classification
     ↓
Analysis
     ↓
Results + JSON Output
     ↓
Annotated Image
```

## Challenges

Some challenges addressed during development include:

-   Separating objects from complex backgrounds
-   Handling image noise
-   Detecting accurate contours
-   Distinguishing squares from rectangles
-   Configuring Python environments and dependencies

## Future Enhancements

The project can be extended by:

-   Replacing rule-based classification with machine learning models
-   Training an ML classifier using extracted geometric features
-   Adding more object categories
-   Using real-world image datasets
-   Adding classification confidence scores
-   Implementing CNN/deep-learning-based classification
-   Developing a GUI or web interface

## Learnings

This project provided practical experience with:

-   OpenCV and computer vision
-   Image preprocessing
-   Feature extraction
-   Modular Python development
-   Software testing
-   Git/GitHub
-   Building a complete computer vision pipeline

## References

-   OpenCV Documentation
-   Python Documentation
-   NumPy Documentation
-   Relevant computer vision textbooks and research papers








