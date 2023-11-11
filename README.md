# Color-Detection-and-Drawing-with-OpenCV
This Python script leverages the OpenCV library to create a real-time color detection and drawing application using a webcam feed. The program identifies specific colors in the video stream and draws circles around the detected color regions.

Features
Adjustable Color Ranges: Easily configure the color detection by modifying the mycolors list, allowing you to detect various colors of interest.

Webcam Settings: The script sets webcam properties such as width, height, and brightness for optimal video capture.

Real-Time Drawing: As the script captures video, it dynamically draws circles around the detected colors on the video feed.

Contour Detection: The color detection is achieved through contour detection in the HSV color space.

Usage
Install Python 3 and the OpenCV library (if not already installed).


pip install opencv-python

python color_detection.py

Explore the webcam feed with real-time color detection and drawing. Press 'q' to exit the application.

Configuration
Adjust the color ranges in the mycolors list to detect different colors.
Notes
Ensure your webcam is connected and accessible.
The script uses a straightforward contour detection method to identify color regions.
Feel free to use and modify this script for your specific projects and applications! Contributions and improvements are welcome.
