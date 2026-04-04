import cv2
from cvzone.HandTrackingModule import HandDetector
import random

hand = HandDetector(detectionCon=0.1)
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")

x1, y1, x2, y2 = 0, 0, 0, 0

x4 = random.randint(100, 380)
y4 = random.randint(100, 540)

def noth(x):
    pass

cv2.createTrackbar("s1", "setting", 0, 400, noth)
cv2.createTrackbar("r", "setting", 0, 255, noth)
cv2.createTrackbar("R", "setting", 0, 255, noth)
cv2.createTrackbar("G", "setting", 0, 255, noth)
cv2.createTrackbar("t", "setting", 1, 10, noth)  # Возможно, для будущих целей

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.rectangle(frame, (x4, y4), (x4 + 50, y4 + 50), (0, 0, 0), -1)

    x3, y3 = 0, 0

    hands, _ = hand.findHands(frame)

    p = cv2.getTrackbarPos("s1", "setting")
    r_color = cv2.getTrackbarPos("r", "setting")
    r_val = cv2.getTrackbarPos("R", "setting")
    g_val = cv2.getTrackbarPos("G", "setting")
    t_value = cv2.getTrackbarPos("t", "setting")

    if hands:
        x2 = hands[0]['lmList'][8][0]
        y2 = hands[0]['lmList'][8][1]
        x1 = hands[0]['lmList'][4][0]
        y1 = hands[0]['lmList'][4][1]

        cv2.circle(frame, (x1, y1), 10, (141, 141, 141), -1)
        cv2.circle(frame, (x2, y2), 10, (141, 141, 141), -1)

        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        print("Distance between fingers:", r)

        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
        cv2.putText(frame, str(round(r, 2)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        if r < 20:
            print("Touch")
            x3 = (x1 + x2) // 2
            y3 = (y1 + y2) // 2
            color = (r_val, g_val, r_color)
            cv2.rectangle(frame, (x3, y3), (x3 + p, y3 + p), color, 2)
        else:
            print("No touch")
    cv2.imshow("setting", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()