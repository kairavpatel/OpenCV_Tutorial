# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:19:31 2019

@author: kaira
"""

import cv2
import numpy as np
import os.path
#import matplotlib.pyplot as plt

def k_means(image,value):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        z = img.reshape(-1,1)
        z = np.float32(z)
        criteria =  (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
        k = value
        ret, label, center = cv2.kmeans(z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
        center =   np.uint8(center)
        res = center[label.flatten()]
        output = res.reshape((img.shape))
        cv2.imshow("Original",image)
        cv2.imshow("Kmeans",output)
        

def main():
    print("Enter the number")
    print("To enter the image   ->1")
    print("To start the video   ->2")
    number = int(input("Press the number : "))
    if number == 1:
        while True:
            path = input ('Enter the image with specific paths...!!\n')
            if os.path.isfile(path) == True:
                img = cv2.imread(path,1)
                img = cv2.resize(img,(700,700))
                num_ = int(input("Press the number of clusters : "))
                k_means(img,num_)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            else:
                print('First file does not exist')
    elif number == 2:
        cap = cv2.VideoCapture(0)
        if  cap.isOpened():
            ret, frame = cap.read()
        else:
            ret = False
        while ret:
            ret, frame = cap.read()
            frame = cv2.resize(frame,(700,700))
            num_ = int(input("Press the number of clusters : "))
            k_means(frame,num_)
            #k_means(frame)
            if cv2.waitKey(1) == 27:
                break
        cv2.destroyAllWindows()
        cap.release()
    else:
        print("Please enter the correct number")

if __name__ == "__main__":
    main()