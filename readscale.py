import cv2 as cv
import os

path_of_photos = "C:\Opencv\photos"
image_name = "\cat.jpeg"
print(os.getcwd())

img = cv.imread(path_of_photos+image_name)
cv.imshow('cat' ,img) 

def rescaleFrame(frame,scale=0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale) 
    dimensions = (width,height)  

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AERA) 

cv.waitKey(0)

#RESCALE VIDEO
import cv2 as cv

path_of_videos = "C:\Opencv\videos"
videos_name =  "\videos.mp4"

capture = cv.VideoCapture('videos/videos.mp4')

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale) 
    dimensions = (width,height) 

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AERA)

#capture = cv.VideoCapture('videos/videos.mp4')


while True:
    isTrue, frame= capture.read()
    frame_resized=rescaleFrame(frame)
cv.imshow('videos',frame)
if cv.waitKey(10) & 0xFF==ord('d'):
    capture.release()

cv.waitKey(0)    
