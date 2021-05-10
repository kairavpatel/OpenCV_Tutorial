# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:48:25 2019

@author: kaira
"""

import cv2
import numpy as np

def main():
        print("===Track Color===")
        print('Enter the number')
        print('Blue color   ->1')
        print('Red color    ->2')
        print('Green color  ->3')
        number = int(input("Press the number : "))
        
        if number == 1:
            #Blue color
            low = np.array([100,50,50])
            high = np.array([140,255,255])
        elif number == 2:
            #Red Clor
            low = np.array([0,100,100])
            high = np.array([10,255,255])
        elif number == 3:
            #Green Color
            low = np.array([40,50,50])
            high = np.array([80,255,255])
        else:
            print('Please enter correct color')
        
        cap = cv2.VideoCapture(0)
        
        if cap.isOpened():
            ret,frame = cap.read()
        else:
            ret = False
        while True:
            ret,frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)##HSV = Hue Saturation Value
            image_mask = cv2.inRange(hsv,low,high)
            output = cv2.bitwise_and(frame, frame, mask = image_mask)
            cv2.imshow("Original_window",frame)
            cv2.imshow("Web_cam",image_mask)
            cv2.imshow("Color_detectoin",output)
            if cv2.waitKey(1) == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
        
if __name__== "__main__":
        main()