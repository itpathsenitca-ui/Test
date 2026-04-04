

import cv2

from cvzone.HandTrackingModule import HandDetector

hand = HandDetector(detectionCon=0.9)
cam = cv2.VideoCapture(0)


while True:
    frame = cam.read()[1]
    frame = cv2.flip(frame, 1)
    h, i = hand.findHands(frame)

    cv2.imshow("setting", frame)
    cv2.waitKey(1)
