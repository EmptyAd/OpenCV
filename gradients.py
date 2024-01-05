import cv2 as cv
import numpy as np

img = cv.imread('Photos/pup.jpeg')
cv.imshow('pup', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sabel
sabelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sabely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sabelx, sabely)

cv.imshow('Sobel x', sabelx)
cv.imshow('sabel y', sabely)
cv.imshow('Sobel', combined_sobel)




cv.waitKey(0)