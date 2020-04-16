##==============================================================================
##   Demo By: Mahnoor Anjum
##   Date: 31/03/2019
##   Codes inspired by:
##   Github.com/imvinod/
##   Official Documentation
##==============================================================================

import numpy as np
import cv2
# Classifier (XML file format)
car = cv2.CascadeClassifier('haarcascades/car.xml')

def detector(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    obj = car.detectMultiScale(gray,1.15,6)
    if obj is ():
        return image
    for (x,y,w,h) in obj:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
    return image

cap = cv2.VideoCapture('imgs/demo5.mp4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Car Detector', detector(frame))
    out.write(detector(frame))
    if cv2.waitKey(1)==13:
        break
out.release()
cap.release()
cv2.destroyAllWindows()
