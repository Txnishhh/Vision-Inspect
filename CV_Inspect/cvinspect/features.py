import cv2
import math

def contour_features(contour, image_shape):
    area = float(cv2.contourArea(contour))
    perimeter = float(cv2.arcLength(contour, True))
    x, y, w, h = cv2.boundingRect(contour)

    moments = cv2.moments(contour)
    if moments["m00"] != 0:
        cx = moments["m10"] / moments["m00"]
        cy = moments["m01"] / moments["m00"]
    else:
        cx, cy = x + w / 2, y + h / 2

    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    vertices = len(approx)

    circularity = (4 * math.pi * area / (perimeter ** 2)) if perimeter else 0.0
    aspect_ratio = w / h if h else 0.0
    extent = area / (w * h) if w and h else 0.0
    image_area = image_shape[0] * image_shape[1]
    relative_area = area / image_area if image_area else 0.0

    return {
        "area": round(area, 2),
        "perimeter": round(perimeter, 2),
        "centroid": {"x": round(cx, 2), "y": round(cy, 2)},
        "bounding_box": {"x": x, "y": y, "width": w, "height": h},
        "vertices": vertices,
        "circularity": round(circularity, 4),
        "aspect_ratio": round(aspect_ratio, 4),
        "extent": round(extent, 4),
        "relative_area": round(relative_area, 6),
    }
