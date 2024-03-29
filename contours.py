import cv2 as cv
import numpy as np 

img = cv.imread('Photos/house.jpeg')
cv.imshow('Pup',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow('contours drawn', blank)
cv.waitKey(0)