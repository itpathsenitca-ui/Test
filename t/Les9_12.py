import cv2
from cvzone.HandTrackingModule import HandDetector

hand = HandDetector(detectionCon=0.1)
# создания переменную для обнаружения руки
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
x1 = 0
y1 = 0
x2 = 0
y2 = 0
SIZE_RECTANGLE = 200

def noth(x):
    print(x)

cv2.createTrackbar("s1", "setting", 0, 400, noth)
cv2.createTrackbar("r", "setting", 0, 255, noth)
cv2.createTrackbar("R", "setting", 0, 255, noth)
cv2.createTrackbar("G", "setting", 0, 255, noth)
cv2.createTrackbar("t", "setting", 0, 255, noth)
r_color = cv2.getTrackbarPos("R", "setting")
g_color = cv2.getTrackbarPos("G", "setting")
b_color = cv2.getTrackbarPos("B", "setting")


# подключили
while True:
    y3 = 0
    x3 = 0
    frame = cam.read()[1]
    hands, i = hand.findHands(frame)
    p = cv2.getTrackbarPos("s1", "setting")
    r_color = cv2.getTrackbarPos("r", "setting")

    print(p)
    if hands:
        x1 = hands[0]['lmList'][4][0]
        y1 = hands[0]['lmList'][4][1]
        x2 = hands[0]['lmList'][8][0]
        y2 = hands[0]['lmList'][8][1]
        cv2.circle(frame, (x1, y1), 10, (141, 141, 141), -1)
        cv2.circle(frame, (x2, y2), 10, (141, 141, 141), -1)
        r = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
        print(r)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)
        cv2.putText(frame,str(r), (50,50), 1, 1,(0,0,0),1)
        if r<20:
            print("touch")
            x3 = (x2 + x1) // 2
            y3 = (y2 + y1) // 2
            cv2.rectangle(frame, (x3, y3), (x3 + p, y3 + p), (r_color, 141, 141), 2)

        else:
            print("not touch")

    cv2.imshow("setting", frame)
    cv2.waitKey(1)
