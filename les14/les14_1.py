from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import cv2

cam = cv2.VideoCapture(0)
hand = HandDetector(detectionCon=0.8)
detector = FaceDetector(minDetectionCon=0.8)

pointHand = 20

def drawPoints(hands, frame):
    global pointHand

    if hands:
        lmList = hands[0]["lmList"]
        total_points = len(lmList)

        pointHand = (pointHand - 1) % total_points

        (x, y, _) = lmList[pointHand]

        cv2.circle(frame, (x, y), 7, (255, 0, 255), -1)

def cvtFrame(frame):
    frame = cv2.flip(frame, 1)
    return frame
def cvtHSV(frame):
    res = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    return res
while True:
    ret,frame = cam.read()
    frame = cvtFrame(frame)
    if not ret:
        break

    img, faces = detector.findFaces(frame, draw=True)
    hands, frame = hand.findHands(frame)

    drawPoints(hands, frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
