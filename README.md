🔊 Gesture-Based Volume Control using OpenCV & MediaPipe
This project enables gesture-based volume control using OpenCV, MediaPipe, and Python. It detects hand gestures via a webcam and adjusts the system volume on macOS based on the distance between the thumb and index finger.

✨ Features:
Real-time Hand Detection using MediaPipe
Volume Control with Finger Gestures (Thumb & Index Finger)
Dynamic Volume Adjustment based on hand movement
Seamless System Integration (macOS osascript for volume control)
Optimized Performance with efficient tracking and processing
🛠️ Tech Stack:
Python
OpenCV (for video processing)
MediaPipe (for hand tracking)
NumPy & Math (for calculations)
AppleScript Integration (macOS volume control)
📌 How It Works:
The script captures live video from the webcam.
Hand landmarks are detected using MediaPipe Hands.
The distance between thumb & index finger is measured.
The volume is dynamically adjusted based on finger spacing.
Visual feedback is displayed, and users can quit by pressing 'q'.
🔗 Usage:
Simply run the script, and adjust your system volume with hand gestures!

🚀 Future Enhancements: Adding Windows/Linux support & voice feedback.

