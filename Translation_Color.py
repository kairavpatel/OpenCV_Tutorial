# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:21:12 2019

@author: kaira
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os.path


def graph(img, title):
   plt.axis('off')
   plt.title(title)
   plt.imshow(img)
   plt.show()

#def zoom_in(img):
#    output = cv2.resize(img, None, 1.5, 1.5) #,interpolation=cv2.INTER_AREA) ##INTER_AREA command for the shrinkage the photo
#    cv2.imshow('output',output)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
#def zoom_out(img,fx,fy):
#    return cv2.resize(img, None, 1.5, 1.5) #, interpolation=cv2.INTER_CUBIC) ##INTER_CUBIC is for the Zooming the photo

def negative_(img):
    return abs(255 - img) ## Conveert the image into Negative image

def Liner_translational(img):
    rows, columns, channels = img.shape
    T = np.float32([[0.5, 0, 50], [0, 0.75, 50]]) ## Linear translational operation
    return cv2.warpAffine(img, T, (columns, rows))

def Rotation_translational(img):
    rows, columns, channels = img.shape
    R = cv2.getRotationMatrix2D((columns/2,rows/2), -45, 1) ## Rotation translational operation
    return cv2.warpAffine(img, R, (columns, rows))

def individual_intensity(img):
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.title("Channel wise distribution of pixel")
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

def total_intensity(img):
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.hist(img.ravel(),256,[0,256])
    plt.title("Total distribution of pixel")
    plt.xlim([0,256])
    plt.show()


def remove_color(img, number):
    if number == 1:
        img[:,:,0] = 0 ##red
        cv2.imshow('Removed Blue',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif number == 2:
        img[:,:,1] = 0 ##Green
        cv2.imshow('Removed Green',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif number == 3:
        img[:,:,2] = 0  ##blue
        cv2.imshow('Removed Red',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('Choose correct color..!!')

def main():
 
 print('Enter the number:')
 #print('==============Zoom the image==================')
 #print('To zoom in                                -> 1')
 #print('To zom out                                -> 2')
 print('===============Translational==================')
 print('For Liner translational                   -> 3')
 print('For Rotation translational                -> 4')
 print('===============Color Section==================')
 print('To see colorwise distribution             -> 5')
 print('To see total distribution                 -> 6')
 print('To see the negative image                 -> 7')
 print('To remove the perticular channel          -> 8')   
 numbers = [int(x) for x in input("Enter multiple values, by separating comma (,): ").split(",")]   
 while True:
    path = input ('Enter the image with specific paths...!!\n')
    if os.path.isfile(path) == True:
       img = cv2.imread(path)
       img = cv2.resize(img,(700,700))
       img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
       graph(img,"Original Image")
       break
    else:
       print('First file does not exist')
 
 for number in range(len(numbers)):
   #if numbers[number] == 1:
      #zoom_in(img)
   #elif numbers[number] == 2:
      #graph(zoom_out(img,fx = 0.5,fy = 0.5),"Increased Image")
   if numbers[number] == 3:
      graph(Liner_translational(img),"Liner Translational")
   elif numbers[number] == 4:
      graph(Rotation_translational(img),"Rotation Translational")
   elif numbers[number] == 5:
      individual_intensity(img) 
   elif numbers[number] == 6:
      total_intensity(img)
   elif numbers[number] == 7:
      graph(negative_(img),"Negative Image")
   elif numbers[number] == 8:
      print('Enter the number')
      print('To remove the Blue     ->1')
      print('To remove the Green    ->2')
      print('To remove the Red      ->3')
      num = int(input('Press the number'))
      remove_color(img, num)
   else:
     print('You did not enter any number')

if __name__=="__main__":
     main()