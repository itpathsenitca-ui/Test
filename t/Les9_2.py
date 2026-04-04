import cv2
from cvzone.HandTrackingModule import HandDetector

hands = HandDetector(detectionCon=0.8)
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)

    head_center = (200, 50)
    head_radius = 30
    body_start = (200, 80)
    body_end = (200, 200)
    left_hand_pos = (150, 130)
    right_hand_pos = (250, 130)
    left_leg_end = (150, 300)
    right_leg_end = (250, 300)

    hands_list, _ = hands.findHands(frame)
    if hands_list:

        hand1 = hands_list[0]
        x_hand1, y_hand1 = hand1['lmList'][9][0], hand1['lmList'][9][1]  # Средняя точка ладони
        cv2.circle(frame, (x_hand1, y_hand1), 10, (0, 255, 0), -1)

        left_hand_pos = (x_hand1, y_han

    if len(hands_list) > 1:
        hand2 = hands_list[1]
        x_hand2, y_hand2 = hand2['lmList'][9][0], hand2['lmList'][9][1]
        right_hand_pos = (x_hand2, y_hand2)

    cv2.circle(frame, head_center, head_radius, (0, 0, 0), -1)
    cv2.line(frame, (200, 80), (200, 200), (0, 0, 0), 2)
    cv2.line(frame, (200, 80), left_hand_pos, (0, 0, 0), 2)
    cv2.line(frame, (200, 80), right_hand_pos, (0, 0, 0), 2)
    cv2.line(frame, (200, 200), (150, 300), (0, 0, 0), 2)
    cv2.line(frame, (200, 200), (250, 300), (0, 0, 0), 2)

    cv2.imshow("Движение рук", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()