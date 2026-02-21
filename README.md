Vision-Based Object Tracking with PID Control

## 📝 Technical Blog

I’ve written a detailed technical explanation of this project here:

🔗 [Read the full blog on Dev.to](https://dev.to/kayampady/vision-based-object-tracking-with-dual-pid-control-4m3l)

The blog explains:
- System architecture
- Dual PID control logic
- Closed-loop design
- Experimental observations

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
