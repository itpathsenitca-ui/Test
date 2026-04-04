import random, os,cvzone,telebot, cv2
from cvzone.FaceMeshModule import FaceMeshDetector

detector = FaceMeshDetector(maxFaces=15)
camera = cv2.VideoCapture(0)
token ="8498232723:AAEoA4CEZBxviiAP_28wwPoKpSGaSLUJEnk"
idBot = 6413829724
bot = telebot.TeleBot(token=token)
while True:
    frame = camera.read()[1]
    img, faces = detector.findFaceMesh(frame)
    imgs = os.listdir("./../imgForBot")
    print(imgs)
    lastIndex = len(imgs)-1
    rand = random.randint(0,100)
    cv2.imwrite(f'./../imgForBot/{imgs[lastIndex]}', frame)
    bot.send_photo(idBot,
                   open(f"./../imgForBot/{imgs[lastIndex]}", "rb"),
                   caption="test")
    #bot.send_message(idBot,f"hello-{rand}")
    cv2.waitKey(1000)