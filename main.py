import cv2
from pid import PID
from vision import detect_blue_object

# PID Controllers
steering_pid = PID(0.005, 0.0001, 0.002)
speed_pid = PID(0.01, 0.0001, 0.005)

# Desired object height (distance reference)
DESIRED_HEIGHT = 300

# Deadband to prevent oscillation
HEIGHT_TOLERANCE = 20

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Vision Detection
    frame, mask, error_x, object_height = detect_blue_object(frame)

    # Default outputs
    steering_output = 0
    speed_output = 0

    # Control Logic
    if error_x is not None and object_height is not None:

        # Steering PID
        steering_output = steering_pid.compute(error_x)

        # Distance Error
        distance_error = DESIRED_HEIGHT - object_height

        # Deadband for stability
        if abs(distance_error) > HEIGHT_TOLERANCE:
            speed_output = speed_pid.compute(distance_error)
        else:
            speed_output = 0

    # Display Info
    cv2.putText(frame, f"Steering: {round(steering_output, 2)}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 2)

    cv2.putText(frame, f"Speed: {round(speed_output, 2)}",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 255), 2)

    cv2.imshow("Mask", mask)
    cv2.imshow("Vision PID Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
