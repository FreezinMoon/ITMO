import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import time
import sys
import os

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=720,
    display_height=480,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink max-buffers=1 drop=true"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


# Process image

def process(image):
    return ~image

#Open Default Camera
cap = cv2.VideoCapture(0) #gstreamer_pipeline(flip_method=4), cv2.CAP_GSTREAMER)

while(cap.isOpened()):
    #Take each Frame
    ret, frame = cap.read()
    
    #Flip Video vertically (180 Degrees)
    frame = cv2.flip(frame, 180)
    
    invert = process(frame)
    cv2.imshow('Cam', invert)
    

    # Exit if "ESC" is pressed
    k = cv2.waitKey(30) & 0xFF
    if k == 27 : #ord 4
        #Quit
        print ('Good Bye!')
        break

#Release the Cap and Video   
cap.release()
cv2.destroyAllWindows()
