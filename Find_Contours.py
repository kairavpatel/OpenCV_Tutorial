# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:11:08 2019

@author: kaira
"""

import cv2
import matplotlib.pyplot as plt
import os.path

def graph(frame, title):
   plt.axis('off')
   plt.title(title)
   plt.imshow(frame)
   plt.show()

def Contoure(img):
   img  =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   ret, thresh = cv2.threshold(gray, 75, 255, 0)
   contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   return cv2.drawContours(img, contours, -1, (0,0,255), 3)
    

def main():
    while True:
     path = input ('Enter the Image with Specify Path...!!\n')
     if os.path.isfile(path) == True:
         img = cv2.imread(path)
         graph(img,'Your choosen figure')
         graph(Contoure(img),"Contours")
         break
     else:
         print('File does not exist')
        
if __name__ == "__main__":
    main()