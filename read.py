#read image
import cv2 as cv
import os
path_of_photos = "C:\Opencv\photos"
image_name =  "\cat.jpeg"
print(os.getcwd())
img = cv.imread(path_of_photos+image_name)
cv.imshow('cat' ,img )
cv.waitKey(0)


#read video
import cv2 as cv
path_of_videos = "C:\Opencv\videos"
videos_name =  "\videos.mp4"

# capture = cv.VideoCapture('videos/videos.mp4')

# whileTrue:
#    isTrue, frame= capture.read()
#     cv.imshow('videos',frame)
#     if cv.waitKey(10) & 0xFF==ord('d'):
#     # capture.release()
#    #  cv.destroyAllWindows()
cv.waitkey(0)


#






