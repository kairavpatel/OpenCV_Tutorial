# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:40:53 2019

@author: kaira
"""

import cv2
import numpy as np
import time
import os.path


def Rotation(img1,img2):
    for i in np.linspace(0,1,100):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0) ## Blending and transii
        cv2.imshow("Converting_image",output)
        time.sleep(0.05)
        if cv2.waitKey(1)==27:
            break
    

def main():
    while True:
        path1 = input ('Enter the first image with specific paths...!!\n')
        if os.path.isfile(path1) == True:
            img1 = cv2.imread(path1,1)
            img1 = cv2.resize(img1,(700,1024))
        else:
            print('First file does not exist')
        path2 = input ('Enter the second image with specific paths...!!\n')
        if os.path.isfile(path2) == True:
            img2 = cv2.imread(path2,1)
            img2 = cv2.resize(img2,(700,1024))
            break
        else:
            print('Second file does not exist')    
    Rotation(img1,img2)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()