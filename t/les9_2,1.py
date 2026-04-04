from distutils.dep_util import newer

import  cv2
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.8)
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
x1 =  0
x2 = 0
y1 = 0
y2 = 0

def noth(x):
    noth(x)
cv2.createTrackbar("s1","setting",0,20,noth)
while True:
    y3 = 0
    x3 = 0
    frame = cam.read()[1]
    h,i =hand.findHands(frame)
    p = cv2.getTrackbarPos("s1", "setting")
    print (p)
    if h:
        x1 = h[0]['lmList'][4][0]
        y1 = h[0]['lmList'][4][1]
        x2 = h[0]['lmList'][8][0]
        y2 = h[0]['lmList'][8][1]
        cv2.circle(frame,(x1,y1),10,(0,0,0),2)
        cv2.circle(frame, (x2, y2), 10, (0, 0, 0), 2)
        r = pow(pow(x1-x2,2)+pow(y1-y2,2),0.5)
        print (r)
        cv2.line(frame,(x1,y1),(x2,y2),(0,0,0),3)
        cv2.putText(frame ,str(r),(50,50), 1,1,(0,0,0),1)
        if r<20:
            print ("touch")
        else:
            print ("not touch")
            x3 = (x2 - x1) // 2
            y3 = (y2 - y1) // 2
        cv2.rectangle(frame,(x3,y3),(200,200),(0,0,0),2)
    cv2.imshow("setting", frame)
    cv2.waitKey(1)
