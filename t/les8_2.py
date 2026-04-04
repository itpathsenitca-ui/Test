import  cv2
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.3)
cam = cv2.VideoCapture(0)
while True:
    frame = cam.read()[1]
    hands,img = hand.findHands(frame)
    cv2.rectangle(frame, (50,50), (200, 200), (255,255,255), -2 )
    cv2.imshow("a", frame)
    cv2.waitKey(1)
