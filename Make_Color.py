# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:52:53 2019

@author: kaira
"""

import cv2
import numpy as np

def emptyfunction():
    pass

def main():
    img1 = np.zeros((512,512,3),np.uint8)
    windowsName = 'Open _cv_Palette'
    cv2.namedWindow(windowsName)
    
    cv2.createTrackbar('B', windowsName, 0, 255, emptyfunction)
    cv2.createTrackbar('G', windowsName, 0, 255, emptyfunction)
    cv2.createTrackbar('R', windowsName, 0, 255, emptyfunction)
    while(True):
        cv2.imshow(windowsName,img1)
        
        if cv2.waitKey(1) == 27:
            break
        blue = cv2.getTrackbarPos('B', windowsName)
        green = cv2.getTrackbarPos('G', windowsName)
        red = cv2.getTrackbarPos('R', windowsName)
         
        img1[:] = [blue,green,red]
    cv2.destroyAllWindows()

if __name__== '__main__':
    main()