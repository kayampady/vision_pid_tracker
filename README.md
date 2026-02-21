Vision-Based Object Tracking with PID Control

# Overview
This project implements real-time blue object tracking using computer vision and dual PID control.

The system:
- Detects a blue object using HSV thresholding
- Computes horizontal deviation from center
- Uses PID to control steering
- Uses object height as distance feedback
- Applies second PID to control speed

# System Architecture

Camera → HSV Threshold → Contour Detection → Error Computation → PID → Control Output

# Key Concepts
 1. Object Detection
- HSV color filtering
- Binary mask generation
- Largest contour extraction

2. Steering Control
Error = object_center_x - frame_center_x  
PID applied to minimize horizontal deviation.

3. Distance Control
Object height used as inverse distance approximation.  
Second PID used to maintain target distance.

# Technologies Used
- Python
- OpenCV
- NumPy

# How to Run
pip install -r requirements.txt  
python main.py

# Future Improvements
- ROS integration
- Kalman filtering
- Real robot motor control
