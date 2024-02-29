# import cv2 as cv
# import os
# path_of_photos = "C:\Opencv\photos"
# image_name = "\cat.jpeg"
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('cat',img)
# print(os.getcwd())
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
# Canny=cv.Canny(img,125,175)
# cv.imshow('canny edges',Canny)
# Contours,hierachies=cv.findContours(Canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(Contours)} Contour(s) found')
# cv.waitKey(0)

import cv2 as cv
import os
path_of_photos = "C:\Opencv\photos"
image_name =  "\cat.jpeg"
img = cv.imread('photos/cat.jpeg')
cv.imshow('cat',img)
print(os.getcwd())
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
Canny=cv.Canny(img,125,175)
cv.imshow('canny edges',Canny)
Contours,hierachies=cv.findContours(Canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(Contours)} Contour(s) found')
cv.waitKey(0)

#threshold
# import cv2 as cv
# import os
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('cat',img)
# print(os.getcwd())
# ret,thresh=cv.threshold(gray,125,225,cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)
# Contours,hierachies=cv.findContours(Canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(Contours)} Contour(s) found')
# cv.waitKey(0)


# import cv2 as cv
# import numpy as np
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('cat',img)
# blank =np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
# blank[:]= 0,255,0
# #ret,thresh=cv.threshold(gray,125,225,cv.THRESH_BINARY)
# # cv.imshow('thresh',thresh)
# Contours,hierachies=cv.findContours(Canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(Contours)} Contour(s) found')
# # cv.waitKey(0)


# cv.drawContours(blank,Contours,-1,(0,0,255),1)
# cv.imshow('contours Drawn',blank)
# cv.waitKey(0)