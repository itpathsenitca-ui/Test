import time
from cvzone.HandTrackingModule import HandDetector
import csv,cv2
detection = HandDetector(detectionCon=0.8)
cam = cv2.VideoCapture(0)
with open("hands1.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["times", "amount of hands"])
    while True:
        frame = cam.read()[1]
        handsDetection,img = detection.findHands(frame)
        if handsDetection:
            amountOfHands = len(handsDetection)
            writer.writerow([(((time.time()/1000)/60)/60), amountOfHands])
        cv2.imshow("Frame", frame)
        cv2.waitKey(1)