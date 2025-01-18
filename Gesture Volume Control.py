import cv2
import numpy as np
import mediapipe as mp
import math
import subprocess  # To execute AppleScript commands for volume control

# Initialize MediaPipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Function to set system volume on macOS using osascript
def set_volume(volume_percentage):
    volume_level = int(volume_percentage / 10)  # macOS volume scale is 0-10
    script = f"set volume output volume {volume_level}"
    subprocess.run(["osascript", "-e", script])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for mirror effect and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame and detect hands
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Ensure hand has at least 9 landmarks before accessing index 4 & 8
            if len(hand_landmarks.landmark) >= 9:
                # Get coordinates of thumb and index finger tips
                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]

                h, w, _ = frame.shape
                x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
                x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

                # Draw circles and a connecting line
                cv2.circle(frame, (x1, y1), 10, (0, 255, 0), -1)
                cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

                # Calculate the Euclidean distance between fingers
                distance = math.hypot(x2 - x1, y2 - y1)

                # Convert distance to volume level (range: 50-300 pixels → 0-100% volume)
                volume_percentage = np.interp(distance, [50, 300], [0, 100])
                set_volume(volume_percentage)  # Adjust macOS system volume

                # Display volume level
                cv2.putText(frame, f'Volume: {int(volume_percentage)}%', (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show output
    cv2.imshow("Gesture Volume Control", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
