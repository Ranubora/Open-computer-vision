import cv2 as cv
path_of_photos ="C:\Opencv\photos"
image_name ="\cat.jpeg"
img = cv.imread(path_of_photos+image_name)
cv.imshow('cat',img )
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#simple thresholding
threshold,thresh=cv.threshold(gray,150,225,)