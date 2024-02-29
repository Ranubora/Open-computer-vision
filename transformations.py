# import cv2 as cv
# import numpy as np
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('cat',img)
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1],img.shape[2])
#     return cv.warpAffine(img,transMat,dimensions)
# translated= translate(img,300,250)

# cv.imshow('translated',translated)
# cv.waitKey(0)


# #rotate
# import cv2 as cv
# #import numpy as np
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('cat',img)
# def rotate(img,angle,rotpoint=None):
#        (height,width) =img.Shape[:2]
#        if rotpoint is None:
#         rotpoint=(width/2,height/2)
#         rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)  
#         dimensions=(width,height)
#         return cv.warpAffine(img,rotMat,dimensions)
# rotated=(img,45)
# rotated_rotated=rotate(rotated,45)
# cv.imshow('rotated_rotated',rotated_rotated)
# #cv.imshow('rotated',rotated)

# cv.waitKey(0)

#RESIZING

# #FLIPPING
# import cv2 as cv
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread('photos/cat.jpeg')
# cv.imshow('cat',img)
# flip=cv.flip(img,0)
# cv.imshow('flip',flip)
# cv.waitKey(0)

#cropping
import cv2 as cv
path_of_photos = "C:\Opencv\photos"
image_name =  "\cat.jpeg"
img = cv.imread('photos/cat.jpeg')
cv.imshow('cat',img)
cropped=img[200:400,300:400]
cv.imshow('cropped',cropped)
cv.waitkey(0)