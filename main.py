import cv2
from pid import PID
from vision import detect_blue_object

pid = PID(0.005, 0.0001, 0.002)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape
    center_x = width // 2

    error, mask, bbox = detect_blue_object(frame)

    steering = 0

    if error is not None:
        steering = pid.compute(error)

        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.line(frame, (center_x, 0), (center_x, height), (0, 0, 255), 2)

    cv2.putText(frame, f"Steering: {round(steering, 3)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Mask", mask)
    cv2.imshow("Vision PID Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
