# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:33:43 2019

@author: kaira
"""

import cv2
import numpy as np
import os.path
windows = 'Drawing'
#inpath = 'C:\\Users\\kaira\\Desktop\\Test\\0_Parade_marchingband_1_12.jpg'
#img = cv2.imread(inpath,1)
#img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windows)
while True:
     path = input ('Enter the Image with Specify Path...!!\n')
     if os.path.isfile(path) == True:
         img = cv2.imread(path,1)
         img = cv2.resize(img,(700,700))
         #graph(img,'Your choosen figure')
         #graph(Contoure(img),"Contours")
         break
     else:
         print('File does not exist')
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,255,0),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,255,255),1)
        #cv2.imshow(windows,img)    

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 40, ( 0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,255,255),1)
        #cv2.imshow(windows,img)    
    blue = img[x,y,0] ### To seprate the image into the different color
    green = img[x,y,1]
    red = img[x,y,2]
    cv2.circle(img, (x,y), 40, ( 0, 255, 0), -1) ## Last(-1) to fill the circle with color
    img1 = np.zeros((512,512,3),np.uint8) ## createt the popup black windows
    img1[:] = [blue,green,red] ### Fill the popup windows with cicked pixel color
    cv2.imshow("Color",img1)    

cv2.setMouseCallback(windows, draw_circle)        
points = []

def main():
    while(True):
        cv2.imshow(windows,img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()    
if __name__ == '__main__':
    main()