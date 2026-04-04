import cv2
cam = cv2.VideoCapture(0)
while True:
    frame = cam.read()[1]
    hsv = cv2.flip(frame,1)
    print(frame)
    cv2.imshow("0-0", frame)
    cv2.imshow("-_-", hsv)
    cv2.waitKey(1)