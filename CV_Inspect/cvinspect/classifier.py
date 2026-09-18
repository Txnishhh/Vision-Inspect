def classify_shape(features):
    v = features["vertices"]
    circularity = features["circularity"]
    aspect = features["aspect_ratio"]
    extent = features["extent"]

    if v == 3:
        return "triangle"

    if v == 4:
        # A near-square rectangle is reported as square.
        if 0.85 <= aspect <= 1.15:
            return "square"
        return "rectangle"

    if circularity >= 0.78 and extent >= 0.65:
        return "circle"

    # Fallback for irregular contours.
    if v > 4 and circularity >= 0.55:
        return "rounded/irregular"

    return "unknown"
