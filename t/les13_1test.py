import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
camera = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1000,minDetectionCon=0.9)
vGog = 0
v = 1
def lookingForAmountFaces(faces,frame):
    global vGog
    global v
    vGog = vGog + 0.10
    print(f'faces:{len(faces)}')
    cv2.putText(frame, f"{len(faces)}", (v, 50), 1, 2, (0, 0, 0), 4)
    print(vGog)
for i in range(pow(10,8)):
    frame = camera.read()[1]
    img, faces = detector.findFaceMesh(frame,draw=True)
    lookingForAmountFaces(faces,frame)
    if faces:
        amount = len(faces[0])
        print(amount)
    if vGog >= 1:
        v+=1
        vGog = 0
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
