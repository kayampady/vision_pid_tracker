import cv2
import numpy as np

def detect_blue_object(frame):
    height, width, _ = frame.shape
    center_x = width // 2

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue color range
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    error_x = 0
    object_height = 0

    if contours:
        largest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest)

        object_center_x = x + w // 2
        error_x = object_center_x - center_x
        object_height = h

        # Draw box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.line(frame, (object_center_x, 0),
                 (object_center_x, height), (255,0,0), 2)

    return frame, mask, error_x, object_height
