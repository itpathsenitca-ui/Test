import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
cam = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1, minDetectionCon=0.8)
for i in range(pow(10, 9)):
    success, frame = cam.read()
    if not success:
        break
    img, faces = detector.findFaceMesh(frame, draw=True)
    if faces:
        amount = len(faces[0])
        print(amount)
        for id, facePoint in enumerate(faces[0], start=0):
            x_center = facePoint[0]
            y_center = facePoint[1]
            if id == 0 or id == 17:
                up_lip_x = facePoint[0]
                up_lip_y = facePoint[1]
                cv2.circle(frame, (int(up_lip_x), int(up_lip_y)), 10, (255, 0, 255), cv2.FILLED)

            if id % 10==0:
                cv2.circle(frame, (int(x_center), int(y_center)), 10, (255, 0, 255), cv2.FILLED)
                cv2.putText(frame, str(id), (int(x_center), int(y_center)), 5, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
