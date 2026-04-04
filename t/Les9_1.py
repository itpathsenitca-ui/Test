import  cv2
from cvzone.HandTrackingModule import HandDetector
from jax.experimental.pallas.ops.tpu.megablox.common import supports_bfloat16_matmul

hand = HandDetector(detectionCon=0.3)
cam = cv2.VideoCapture(0)
cv2.namedWindow("setting")
def nothing(x):
    print(x)
cv2.createTrackbar("s1","setting",0,20,nothing)
while True:
    frame = cam.read()[1]
    hands,img = hand.findHands(frame)
    p = cv2.getTrackbarPos("s1","setting")
    print(p)
    if hands:
        x = hands[0]['lmList'][p][0]
        y = hands[0]['lmList'][p][1]
        cv2.circle(frame,(x,y),20,(255,255,255),cv2.FILLED)
        print(hands[0]['lmList'][2][0])
        if hands:
            x = hands[0]['lmList'][2][0]
            y = hands[0]['lmList'][2][1]
            cv2.circle(frame, (x, y), 10, (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f"X: {x} Y: {y}", (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imshow("setting", frame)
    cv2.waitKey(1)
