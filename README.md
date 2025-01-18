# Gesture Volume Control using OpenCV & MediaPipe

## 📌 Project Description
This project allows users to control the system volume using hand gestures. It utilizes OpenCV for video capture, MediaPipe for hand tracking, NumPy for calculations, and Subprocess to adjust system volume dynamically based on the distance between the thumb and index finger.


## ✨ Features
- Real-time hand tracking using MediaPipe
- Gesture-based volume control
- Dynamic volume adjustment based on finger distance
- Works on Windows (Linux/Mac support may vary)

## 📦 Installation & Requirements
Run the following command to install the necessary dependencies:

```bash
pip install opencv-python numpy mediapipe
```

For Windows users, download and place `nircmd.exe` in the project folder to control system volume.

## ⚙️ How It Works
1. OpenCV captures the video feed from the webcam.
2. MediaPipe detects hand landmarks and extracts key points.
3. The distance between the thumb and index finger is calculated using `math.dist()`.
4. Volume is mapped proportionally to the distance and adjusted using `subprocess`.
5. The updated volume level is displayed on the screen.

## 🖥️ Usage
Run the script using:

```bash
python gesture_volume_control.py
```
- Ensure the webcam is connected.
- Move your thumb and index finger closer/farther to adjust the volume.
- Press `q` to exit.


## 🔧 Troubleshooting
- **Camera not working?** Ensure no other applications are using the webcam.
- **Volume not changing?** Ensure `nircmd.exe` is installed correctly (Windows users).
- **Slow performance?** Reduce `min_detection_confidence` in `mp.solutions.hands`.

## 📜 License
This project is open-source under the MIT License.

## 🤝 Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

