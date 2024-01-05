import cv2 as cv

img = cv.imread('Photos/pup.jpeg')
cv.imshow('Pup', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshs', thresh_inv)

#adaptive thresholding
adaptive_thrsh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3 )
cv.imshow('adaptive', adaptive_thrsh)   






cv.waitKey(0)