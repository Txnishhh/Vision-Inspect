import cv2

def find_external_contours(mask):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    return sorted(contours, key=cv2.contourArea, reverse=True)

def filter_contours(contours, min_area=300):
    return [c for c in contours if cv2.contourArea(c) >= min_area]
