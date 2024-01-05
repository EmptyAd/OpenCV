import cv2 as cv

img = cv.imread('Photos/group.jpeg')
cv.imshow('person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors= 6)

print(f'No of faces = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('detected', img)


cv.waitKey(0)