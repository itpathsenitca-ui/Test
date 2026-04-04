import cv2, serial
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
uno = serial.Serial("COM7", 9600, timeout=0.1)
cam = cv2.VideoCapture(0) #подкл камеру
kX = 3.5 # коэфицент
kY = 2.6
cv2.namedWindow("turret")
while True:
    frame = cam.read()[1] #
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # в серый
    faces = face.detectMultiScale(gray,1.3,5,1,(10,10))#цвет scaleFactor min
    if len(faces)>0:#проверка есть ли лица
        print(faces[0])
        [x,y,w,h] = faces[0]#ширина высота и тд
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        angles0fServo = f"x{x//kX}y{y//kY}"
        print(angles0fServo)
        uno.write(angles0fServo.encode())
    cv2.imshow("turret", frame)
    cv2.waitKey(1)