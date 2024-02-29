import cv2 as cv
import numpy as np

path_of_photos ="C:\Opencv\photos"
image_name ="\cat.jpeg"
img = cv.imread(path_of_photos+image_name)
cv.imshow('cat',img )
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#laplacian
Lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(Lap))
cv.imshow('Laplacian',Lap)

#sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobel X',sobelx)
cv.imshow('sobel Y',sobely)


#sobel combined
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel X',sobelx)
cv.imshow('sobel Y',sobely)
canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)
cv.waitKey(0)


