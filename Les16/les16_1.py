from matplotlib.patches import bbox_artist

from data import bot, idBot
from cvzon_helper import detector
from cv2_helper import cam,cv2, cvtColor_helper_HLS
while True:
   frame = cam.read()[1]
   _,faces = detector.findFaces(frame,idBot)  
   if faces:
      cv2.imwrite("./img/face.jpg",cvtColor_helper_HLS(frame))
      bot.send_photo(idBot,open("./img/face.jpg","rb"),caption="")
      print("face detected")
      bbox = faces[0]['bbox']
      [x,y,w,h] = bbox
      face_test = frame[y:y+h,x:x+w]
      cv2.imwrite("./img/test.jpg",face_test)
   else:
      print("No faces detected")
   cv2.imshow('frame',frame)
   cv2.waitKey(1)