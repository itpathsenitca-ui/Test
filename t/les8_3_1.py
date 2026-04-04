import  cv2
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.3)
cam = cv2.VideoCapture(0)
xR = 50
yR = 50
while True:
    frame = cam.read()[1]
    hands,img = hand.findHands(frame)
    if hands:
        print(hands[0]['lmList'][0][0])
        xR = hands[0]['lmList'][8][0]
        yR = hands[0]['lmList'][8][1]

    cv2.rectangle(frame, (xR+50,yR+50), (xR, yR), (255,255,255), -2 )
    cv2.imshow("a", frame)
    cv2.waitKey(1)
