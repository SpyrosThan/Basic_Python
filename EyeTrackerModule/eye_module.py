from pickle import TRUE
import cv2
import numpy as np


def eyeTrack(blue,green,red):
    cap = cv2.VideoCapture(0)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    while True:
        ret, frame=cap.read()
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        eyes = eye_cascade.detectMultiScale(gray, 1.2, 4)
        for(x,y,width,height) in eyes:
            cv2.rectangle(frame,(x,y),(x+width, y+height), (blue,green,red),5)
        cv2.imshow('frame', frame)
    
    
        if cv2.waitKey(1) == ord('s'):
            break

    cap.release()
    cv2.destroyAllWindows()
