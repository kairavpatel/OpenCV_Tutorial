# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:42:18 2019

@author: kaira
"""

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    ret, frame1 = cap.read()    
    ret, frame2 = cap.read()
    
    while ret:
        d = cv2.absdiff(frame2,frame1)
        grey =  cv2.cvtColor(d,cv2.COLOR_BGR2GRAY) ## Converting the into gray scale
        blur = cv2.GaussianBlur(grey, (5,5), 0) ## Creating th eblur into the Image
        ret,th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY) ## Image with Binary thresold
        dilated = cv2.dilate(th, np.ones((3,3), np.uint8), iterations = 15)
        eroded = cv2.erode(dilated, np.ones((3,3), np.uint8), iterations = 15)
        contours, hierarchy =  cv2.findContours(eroded,  cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame1, contours, -1, (0,0,255), 3)
               
        cv2.imshow("Original",frame2)
        cv2.imshow("INtermediate",frame1)
        if cv2.waitKey(1) == 27:
            break
        frame1 = frame2
        ret,frame2 = cap.read()
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()
            