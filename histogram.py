import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/pup.jpeg')
cv.imshow('pup', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#gray scale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Gray Scale')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show

cv.waitKey(0)