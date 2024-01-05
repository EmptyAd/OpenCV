import cv2 as cv

img = cv.imread('Photos/pup.jpeg')
cv.imshow('dog',img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur= cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edge cascade
edge= cv.Canny(img, 125, 175)
cv.imshow('edge', edge)

#dilating the image
dil = cv.dilate(edge, (7,7), iterations=4)
cv.imshow('dil', dil)





cv.waitKey(0)