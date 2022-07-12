#Eye Tracker Module - Coded by Spy (Github) - Code is completely open source, you can change it and even use it however you want#
from pickle import TRUE
import cv2
import numpy as np


def eyeTrack(blue,green,red):
    capture = cv2.VideoCapture(0)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    while True:
        ret, img=capture.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        eyes = eye_cascade.detectMultiScale(gray, 1.2, 4)
        for(x,y,width,height) in eyes:
            cv2.rectangle(img,(x,y),(x+width, y+height), (blue,green,red),5)
        cv2.imshow('frame', img)
    
    
        if cv2.waitKey(1) == ord('s'):
            break

    capture.release()
    cv2.destroyAllWindows()
