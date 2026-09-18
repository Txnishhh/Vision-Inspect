from .preprocessing import preprocess
from .segmentation import find_external_contours, filter_contours
from .features import contour_features
from .classifier import classify_shape

def analyze_image(image, min_area=300):
    stages = preprocess(image)
    contours = find_external_contours(stages["mask"])
    contours = filter_contours(contours, min_area=min_area)

    detections = []
    for contour in contours:
        features = contour_features(contour, image.shape)
        detections.append({
            "shape": classify_shape(features),
            "features": features,
        })

    summary = {}
    for item in detections:
        shape = item["shape"]
        summary[shape] = summary.get(shape, 0) + 1

    report = {
        "image": {
            "width": int(image.shape[1]),
            "height": int(image.shape[0]),
            "channels": int(image.shape[2]) if len(image.shape) == 3 else 1,
        },
        "objects_detected": len(detections),
        "shape_summary": summary,
        "detections": detections,
    }
    return report, stages
