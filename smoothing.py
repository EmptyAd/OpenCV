import cv2 as cv
import numpy as np

img = cv.imread('Photos/pup.jpeg')
cv.imshow('Pup', img)

#averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#gaussian
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss', gaussian)

#medium blur
medium = cv.medianBlur(img, 3)
cv.imshow('medium', medium)

#bilateral blur
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
