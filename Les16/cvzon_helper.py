from cvzone.FaceDetectionModule import FaceDetector
import cv2

cam = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.8)