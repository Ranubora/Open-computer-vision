# import cv2 as cv
# path_of_photos ="C:\Opencv\photos"
# image_name ="\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img)
# b,g,r=cv.split(img)
# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)
# print(b.shape)
# print(g.shape)
# print(r.shape)

# merged=cv.merge([b,g,r])
# cv.imshow('merged image',merged)
# cv.waitKey(0)

import cv2 as cv
import numpy as np

path_of_photos ="C:\Opencv\photos"
image_name ="\cat.jpeg"
img = cv.imread(path_of_photos+image_name)
cv.imshow('cat',img)
blank =np.zeros(img.shape[:2],dtype='uint8')
b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])


cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow('merged image',merged)
cv.waitKey(0)
