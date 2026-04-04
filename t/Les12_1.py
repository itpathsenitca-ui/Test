import cv2, random
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.8)
cam = cv2.VideoCapture(0)
cv2.namedWindow('setting')
y = 0
x = 0
speed = 1
SIZE = 100
def nothing(x):
    print(x)
cv2.createTrackbar("x", "setting", 0, 640, nothing)
cv2.createTrackbar("y", "setting", 0, 480, nothing)
def createRectangle():
    p = cv2.getTrackbarPos("x", "setting")
    p1 = cv2.getTrackbarPos("y", "setting")
    cv2.rectangle(frame, (p1, p), (p1 + 50, p + 50), (255, 0, 0), -1)

def randomShowRectangle(x,y, size):
     cv2.rectangle(frame, (x, y), (x + size, y + size), (255, 0, 0), -1)
while True:
    frame = cam.read()[1]
    frame = cv2.flip(frame, 1)
    h, i = hand.findHands(frame)
    randomShowRectangle(50,y, SIZE)
    # createRectangle() for create our rectangle
    createRectangle()
    cv2.imshow('setting', frame)
    cv2.waitKey(1)
    speed=+1
    if y > 480:
        speed+=3
        y = -50
        x = random.randint(0,480)
