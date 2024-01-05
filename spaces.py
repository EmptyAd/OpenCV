import cv2 as cv

img = cv.imread('Photos/pup.jpeg')
cv.imshow('House', img)

#BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', RGB)

cv.waitKey(0)