#CONVERT IN GRAY COLOR
# import cv2 as cv
# import os
# path_of_photos ="C:\Opencv\photos"
# image_name ="\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img )
# print(os.getcwd())
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
# cv.waitKey(0)

#BLUR IMAGE
#import cv2 as cv
# path_of_photos ="C:\Opencv\photos"
# image_name ="\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img )
# blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
# cv.waitKey(0)

#EDGE CASCADE
# import cv2 as cv
# path_of_photos ="C:\Opencv\photos"
# image_name ="\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img )
# Canny=cv.Canny(img,125,175)
# cv.imshow('canny edges',Canny)
# cv.waitKey(0)

# #BLUR EDGES


 #DILATING A IMAGE
# # import cv2 as cv
# # path_of_photos ="C:\Opencv\photos"
# # image_name ="\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img )
# Canny=cv.Canny(img,125,175)
# cv.imshow('canny edges',Canny)
# Dilated=cv.dilate(Canny,(3,3),iterations=1)
# cv.imshow('Dilated',Dilated)
# cv.waitKey(0)

#ERODED A IMAGE
# import cv2 as cv
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img )
# Canny=cv.Canny(img,125,175)
# cv.imshow('canny edges',Canny)
# Dilated=cv.dilate(Canny,(3,3),iterations=1)
# cv.imshow('Dilated',Dilated)
# Eroded=cv.erode(Dilated,(3,3),iterations=1)
# cv.imshow('Eroded',Eroded)
# cv.waitKey(0)

# #RESIZE A IMAGE
# import cv2 as cv
# import os
# path_of_photos ="C:\Opencv\photos"
# image_name ="\lady.jpg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('lady',img )
# print(os.getcwd())
# resized=cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
# cv.imshow('resized',resized)
# cv.waitKey(0)

#CROPPING A IMAGE
import cv2 as cv
import os
path_of_photos ="C:\Opencv\photos"
image_name ="\cat.jpeg"
img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img )
# print(os.getcwd())
# Canny=cv.Canny(img,125,175)
# cv.imshow('canny edges',Canny)
# Dilated=cv.dilate(Canny,(3,3),iterations=1)
# cv.imshow('Dilated',Dilated)
# Eroded=cv.erode(Dilated,(3,3),iterations=1)
# cv.imshow('Eroded',Eroded)
resized=cv.resize(img,(700,700),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)
Cropped = img[100:300, 200:700]
cv.imshow('Cropped',Cropped)
cv.waitKey(0)


