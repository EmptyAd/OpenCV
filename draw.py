import cv2 as cv
import numpy as np

#(height,width, no of colour/scheme)
blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('blank' , blank)

# 1. paint the image a certain colour
# blank[200:300,300:400] = 0,0,255 #l[range of pixels] = colour scheme of bgr
#cv.imshow('Green', blank)

#2. draw rectangle
cv.rectangle(blank, (0,0),(250,250),(0,0,255),thickness=2)
cv.imshow('Rectanle',blank)

#3. circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness=2)
cv.imshow('cirle', blank)
# img = cv.imread('Photos/pup.jpeg')
# cv.imshow('pic', img)

cv.waitKey(0)