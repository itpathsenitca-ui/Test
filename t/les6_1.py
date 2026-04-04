import serial, cv2
port = "COM7"
speed = 9600
uno = serial.Serial(port,speed,timeout=0.1)


while True:
    v = input("Enter any angle of servo: ")
   # print(v)
    uno.write(v.encode())
    cv2.waitKey(1)
