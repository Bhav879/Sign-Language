import cv2
import mediapipe as mp

# Use mediapipe solutions safely
hands_module = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

with hands_module.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
) as hands:

    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to read from webcam")
            break

        # Flip for mirror effect (optional but nice)
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks
                drawing_utils.draw_landmarks(
                    frame,
                    hand_landmarks,
                    hands_module.HAND_CONNECTIONS
                )

                # Print first 5 landmarks only
                h, w, _ = frame.shape
                lm_list = []
                for i, lm in enumerate(hand_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append((i, cx, cy))

                print("Landmarks:", lm_list[:5])

        cv2.imshow("Hand Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
