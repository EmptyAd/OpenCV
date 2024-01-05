import cv2 as cv
import numpy as np

blank = cv.imread('Photos/land.jpeg')
cv.rectangle(blank, (100,250),(300,500),(0,0,255),thickness=2)
cv.rectangle(blank, (300,250),(700,500),(0,0,255),thickness=2)
cv.rectangle(blank, (150,500),(250,350),(0,0,255),thickness=2)
cv.rectangle(blank, (400,300),(600,425),(0,0,255),thickness=2)
cv.line(blank,(100,250),(200,50),(0,0,255),thickness=2)
cv.line(blank,(300,250),(200,50),(0,0,255),thickness=2)
cv.line(blank,(700,250),(600,50),(0,0,255),thickness=2)
cv.line(blank,(200,50),(600,50),(0,0,255),thickness=2)
cv.line(blank,(400,362),(600,362),(0,0,255),thickness=2)
cv.line(blank,(500,300),(500,425),(0,0,255),thickness=2)
cv.circle(blank,(200,200),30,(0,0,255),thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)