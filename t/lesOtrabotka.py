import  cv2
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.3)
cam = cv2.VideoCapture(0)
while True:
    frame = cam.read()[1]
    hands,img = hand.findHands(frame)
    cv2.rectangle(frame, (50,50), (200, 200), (255,255,255), -2 )
    if hands:
         points = hands[0]["lmList"]
         #print(points)
         point = points[2]
         x = point[0]
         y = point[1]

         point1 = points[4]
         x1 = point1[0]
         y1 = point1[1]
         cv2.putText(frame,"yes",(x,y), 1,2,(0,0,0), 2)
         cv2.putText(frame,"why",(x,y), 1,2,(0,0,0), 2)
         print(point)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
