# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:38:29 2019

@author: kaira
"""

import cv2
import numpy as np


def MAX_RGB(img):
    (B,G,R) = cv2.split(img)
    M = np.maximum(np.maximum(R,G),B)
    R[ R < M] = 0
    G[ G < M] = 0
    B[ B < M] = 0
    return cv2.merge((B, G ,R))
        


def main():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame= cap.read()
    else:
        ret = False
    while ret:
        
        ret,frame = cap.read()
        output = MAX_RGB(frame)
        cv2.imshow("Video",output)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()
if __name__ == "__main__":
    main()  