import cv2
cam = cv2.VideoCapture(0)

def cvtColor_helper_RGB(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)

def cvtColor_helper_HSV(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV, frame)

def cvtColor_helper_HLS(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HLS, frame)

def cvtColor_helper_GRAY(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY, frame)

