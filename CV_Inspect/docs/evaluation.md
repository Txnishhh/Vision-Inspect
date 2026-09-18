# Dataset, Model Selection & Evaluation

## Dataset
`data/sample_shapes.png` is a controlled synthetic image containing circles, squares, rectangles and triangles on a clean background.

## Model Selection
No trained ML model is used. Classical OpenCV and a rule-based classifier are used because contour vertex count, circularity, aspect ratio and extent directly describe the target shapes.

## Evaluation Methodology
For labeled images, compare predictions with ground truth. Accuracy = correct/total; Precision = TP/(TP+FP); Recall = TP/(TP+FN). `cvinspect/evaluation.py` implements these metrics.

## Limitations
Results depend on contrast, noise, object separation, scale and occlusion.
