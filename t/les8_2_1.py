import  cv2
from cvzone.HandTrackingModule import HandDetector
hand = HandDetector(detectionCon=0.3)
cam = cv2.VideoCapture(0)
cv2.namedWindow('g')
def noth(x):
    print(x)
cv2.createTrackbar('g', 'g', 0, 255, noth)
cv2.createTrackbar('E', 'g', 0, 255, noth)
while True:
    frame = cam.read()[1]
    hands,img = hand.findHands(frame)
    xR = cv2.getTrackbarPos('g', 'g')
    yR = cv2.getTrackbarPos('E', 'g')
    cv2.rectangle(frame, (xR+50, yR+50), (xR+200, yR+200), (255,255,255), -2 )
    cv2.imshow("a", frame)
    cv2.waitKey(1)
