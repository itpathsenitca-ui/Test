import random

import cv2

from cvzone.HandTrackingModule import HandDetector

hands = HandDetector(detectionCon=0.8)
cam = cv2.VideoCapture(0)

x1 = 0
x2 = 0
y1 = 0
y2 = 0
while True:
    frame = cam.read()[1]
    frame = cv2.flip(frame, 1)
    cv2.line(frame, (200, 50), (200, 200), (0, 0, 0), 10)
    cv2.line(frame, (200, 200), (150, 300), (0, 0, 0), 2)
    cv2.line(frame, (200, 200), (250, 300), (0, 0, 0), 2)
    cv2.circle(frame, (200, 50), 30, (0, 0, 0), -1)
    h, i = hands.findHands(frame)
    cv2.line(frame, (185, 50), (100, 80), (255, 255, 255), 10)
    cv2.line(frame, (220, 50), (100, 80), (255, 255, 255), 10)
    if h:
        cv2.circle(frame, (185, 50), 10, (255, 255, 255), -1)
        cv2.circle(frame, (220, 50), 10, (255, 255, 255), -1)
        x = h[0]['lmList'][8][0]
        y = h[0]['lmList'][8][1]
        cv2.line(frame, (200, 80), (x, y), (0, 0, 0), 2)
        cv2.line(frame, (200, 80), (x, y), (0, 0, 0), 2)
        for id,i in enumerate(h[0]["lmList"],0):
            (x,y,d) = i
            cv2.circle(frame,(x,y),10,(255,255,255),-1)
            cv2.putText(frame, str(id), (x-5,y+5),1, 1, (0,0,0), 2)
            print(id,i)

        cv2.putText(frame, "1", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, "2", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow("setting", frame)
    cv2.imshow("setting", frame)
    cv2.waitKey(1)
