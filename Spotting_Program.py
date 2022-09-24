#Shrikant Pawar, 03/06/2020, Car counter program for Propark
#!/usr/bin/python
#First-level obfuscation: python -OO -m py_compile <your program.py>
#rtsp://Shrikant:Shri@2020@50.208.156.204:7001/Streaming/channels/102
#/Users/yalegenomecenter/Desktop/vehicle_counting_tensorflow-master/Revision 03_08_2020/images/Road traffic video for object recognition.mp4
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import os
from cvlib.object_detection import draw_bbox
import numpy as np
import time
from tkinter import *
os.chdir('/Users/pawar/Desktop/Revision 03_08_2020/images')
vid = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture('/Users/pawar/Desktop/Revision 03_08_2020/images/Road traffic video for object recognition.mp4')
vid3 = cv2.VideoCapture('/Users/pawar/Desktop/Revision 03_08_2020/images/camera3.mp4')
vid4 = cv2.VideoCapture('/Users/pawar/Desktop/Revision 03_08_2020/images/camera4.mp4')
'''
if not os.path.exists('images'):
    os.makedirs('images')
'''
index = 0
while(True):
    ret, frame = vid.read()
    ret2, frame2 = vid2.read()
    ret3, frame3 = vid3.read()
    ret4, frame4 = vid4.read()
    if not ret: 
        break
        print('Video ended unexpectedly..')
    name = 'frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    print(name)    
    im = cv2.imread(name)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    #print('Number of cars in the image is '+ str(label.count('car')))
    #print('Number of trains in the image is '+ str(label.count('train')))
    #print('Number of trucks in the image is '+ str(label.count('truck')))
    car = str(label.count('car'))
    train = str(label.count('train'))
    truck = str(label.count('truck'))
    total = [int(car),int(train),int(truck)]
    print('Total number of cars parked in camera 1: ' + str(sum(total)))
    cv2.imshow("Frame", output_image)

    name2 = 'frame2' + str(index) + '.jpg'
    print ('Creating...' + name2)
    cv2.imwrite(name2, frame2)
    print(name2)    
    im2 = cv2.imread(name2)
    bbox2, label2, conf2 = cv.detect_common_objects(im2)
    output_image2 = draw_bbox(im2, bbox2, label2, conf2)
    #print('Number of cars in the image is '+ str(label.count('car')))
    #print('Number of trains in the image is '+ str(label.count('train')))
    #print('Number of trucks in the image is '+ str(label.count('truck')))
    car2 = str(label2.count('car'))
    train2 = str(label2.count('train'))
    truck2 = str(label2.count('truck'))
    total2 = [int(car2),int(train2),int(truck2)]
    print('Total number of cars parked in camera 2: ' + str(sum(total2)))
    cv2.imshow("Frame2", output_image2)
    
    name3 = 'frame3' + str(index) + '.jpg'
    print ('Creating...' + name3)
    cv2.imwrite(name3, frame3)
    print(name3)    
    im3 = cv2.imread(name3)
    bbox3, label3, conf3 = cv.detect_common_objects(im3)
    output_image3 = draw_bbox(im3, bbox3, label3, conf3)
    #print('Number of cars in the image is '+ str(label.count('car')))
    #print('Number of trains in the image is '+ str(label.count('train')))
    #print('Number of trucks in the image is '+ str(label.count('truck')))
    car3 = str(label3.count('car'))
    train3 = str(label3.count('train'))
    truck3 = str(label3.count('truck'))
    total3 = [int(car3),int(train3),int(truck3)]
    print('Total number of cars parked in camera 3: ' + str(sum(total3)))
    cv2.imshow("Frame3", output_image3)

    name4 = 'frame4' + str(index) + '.jpg'
    print ('Creating...' + name4)
    cv2.imwrite(name4, frame4)
    print(name4)    
    im4 = cv2.imread(name4)
    bbox4, label4, conf4 = cv.detect_common_objects(im4)
    output_image4 = draw_bbox(im4, bbox4, label4, conf4)
    #print('Number of cars in the image is '+ str(label.count('car')))
    #print('Number of trains in the image is '+ str(label.count('train')))
    #print('Number of trucks in the image is '+ str(label.count('truck')))
    car4 = str(label4.count('car'))
    train4 = str(label4.count('train'))
    truck4 = str(label4.count('truck'))
    total4 = [int(car4),int(train4),int(truck4)]
    print('Total number of cars parked in camera 4: ' + str(sum(total4)))
    cv2.imshow("Frame4", output_image4)
    cv2.waitKey(200)
    index += 1
    time.sleep(15)

    for file in os.listdir('.'):
        if file.endswith('.jpg'):
            os.remove(file) 

    
