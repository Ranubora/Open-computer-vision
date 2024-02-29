import cv2 as cv

path_of_photos = "C:\Opencv\photos"
image_name =  "\cat.jpeg"
img = cv.imread(path_of_photos+image_name)
cv.imshow('cat',img)
#BGR TO GRAYSCALE
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
#BGR TO L*a*b
Lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',Lab)
#BGR TO RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

cv.waitKey(0)


# import cv2 as cv
# import matplotlib.pyplot as plt
# path_of_photos = "C:\Opencv\photos"
# image_name =  "\cat.jpeg"
# img = cv.imread(path_of_photos+image_name)
# cv.imshow('cat',img)
# plt.imshow(img)
# #plt.imshow()
# cv.waitKey(0)

