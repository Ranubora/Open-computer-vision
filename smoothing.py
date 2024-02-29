import cv2 as cv
path_of_photos = "C:\Opencv\photos"
image_name = "\cat.jpeg"
img = cv.imread(path_of_photos+image_name)
cv.imshow('cat' ,img )

#averaging
average =cv.blur(img,(3,3))
cv.imshow('average blur',average)

#Gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#median blur
median=cv.MedianBlur(img,1)
cv.imshow('Median Blur', median)

#bilateral 
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)