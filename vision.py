import cv2
import numpy as np

def detect_blue_object(frame):
    height, width, _ = frame.shape
    frame_center_x = width // 2

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    error = 0

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 500:
            x, y, w, h = cv2.boundingRect(largest)
            object_center_x = x + w // 2

            error = object_center_x - frame_center_x

            return error, mask, (x, y, w, h)

    return None, mask, None
