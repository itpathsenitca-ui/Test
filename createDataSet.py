import cv2, time, os
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.7)
saveInterval = 0.5
lastTime = time.time()
countImg = 0
basicDirectory = "dataset502"
folderName = "Maxim"
path = os.path.join(basicDirectory, folderName)
os.makedirs(path)
while True:
    success, img = cap.read()
    img, boxes = detector.findFaces(img)
    print(boxes)
    if len(boxes)==1:
        face = boxes[0]["bbox"]
        (x,y,w,h) = face
        imgFace = img[y:y+h, x:x+w]
        print(img)
        currentTime = time.time()
        if - lastTime + currentTime> saveInterval:
            print(f"save{countImg}")
            countImg+=1
            fileName = f"{folderName}{countImg}.jpg"
            filepath = os.path.join(path,fileName )
            cv2.imwrite(filepath, imgFace)
            lastTime = currentTime
            cv2.imshow("face", imgFace)
    cv2.putText(img,f"save img: {countImg}", (50,50),1, 2, (255,0,0),2)
    cv2.imshow("Head/Face Detection - cvzone", img)
    cv2.waitKey(1)

