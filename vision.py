import cv2
import numpy as np


def detect_blue_object(frame, min_area=800):
    """
    Detects largest blue object in frame.

    Returns:
        frame          -> annotated frame
        mask           -> binary mask
        error_x        -> horizontal error (None if not found)
        object_height  -> bounding box height (None if not found)
    """

    height, width, _ = frame.shape
    frame_center_x = width // 2

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue color range (tunable)
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # Threshold
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Noise reduction
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return frame, mask, None, None

    # Largest contour
    largest = max(contours, key=cv2.contourArea)

    area = cv2.contourArea(largest)

    if area < min_area:
        return frame, mask, None, None

    # Bounding box
    x, y, w, h = cv2.boundingRect(largest)

    object_center_x = x + w // 2
    error_x = object_center_x - frame_center_x
    object_height = h

    # ---- Visualization ----
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.line(frame, (frame_center_x, 0),
             (frame_center_x, height), (0, 0, 255), 2)
    cv2.line(frame, (object_center_x, 0),
             (object_center_x, height), (255, 0, 0), 2)

    cv2.putText(frame, f"Error X: {error_x}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2)

    cv2.putText(frame, f"Height: {object_height}",
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2)

    return frame, mask, error_x, object_height
