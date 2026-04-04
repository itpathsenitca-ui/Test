import cv2, os, numpy as np, pickle
from imutils import paths

basicFolder = "dataset502"
faces = []
labelMap = {}
numberFace = 0
labels = [0]
print(os.listdir("dataset502"))
for personName in os.listdir(basicFolder):
    personFolder = os.path.join(basicFolder,personName)
    imgsFolder = list(paths.list_images(personFolder))
    print(imgsFolder)
    labelMap[numberFace] = personName

    for img in imgsFolder:
        imgCurrent = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
        # gray = cv2.cvtColor(imgCurrent)
        resultImg = cv2.resize(imgCurrent, (200,200))
        faces.append(resultImg)
        numberFace += 1
print(labelMap)
recognayser = cv2.face.LBPHFaceRecognizer_create(
    neighbors=8,
    radius=2,
    grid_x=8,
    grid_y=8,
    threshold=80


)
print("qwdfw")
recognayser.train(faces,np.array(labels))
