import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')
cap = cv.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors= 3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=2)

         
    cv.imshow('img',img)
    k = cv.waitKey(30) & 0xff
    if k == 27:      #Press Esc to stop the video
        break

cap.release()
