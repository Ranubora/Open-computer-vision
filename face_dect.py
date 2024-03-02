

import cv2 as cv
img=cv.imread('photos/lady.jpg')
cv.imshow('person',img)
resized=cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.waitKey(0)
