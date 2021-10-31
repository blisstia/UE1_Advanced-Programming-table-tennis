# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:12:03 2021

@author: Chenyin WU
"""

##############################################################################
# Table tennis position detection under ideal conditions                     #
# Hough circle tracking                                                      #
##############################################################################


import cv2
import numpy as np

def Hough_circle(imgGray, canvas):
    global Hough_x, Hough_y
    img = cv2.medianBlur(imgGray, 3)
    img = cv2.GaussianBlur(img, (17, 19), 0)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 1000,
                               param1=50, param2=15, minRadius=3, maxRadius=7)
    try:
        circles = np.uint16(np.around(circles))
    except:
        pass
    else:
        for i in circles[0, :]:
            cv2.circle(canvas, (i[0], i[1]), i[2], (255, 100, 0), 2)
            cv2.circle(canvas, (i[0], i[1]), 2, (0, 0, 255), 3)
            Hough_x = i[0]
            Hough_y = i[1]

frameWidth = 960
frameHeight = 544
cap = cv2.VideoCapture('/Users/tia/Desktop/UE1_projet/dataset/test/videos/Pingpong.mp4')
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 80) 
pulse_ms = 30

Hough_x = 0
Hough_y = 0 
HoughXs = []
HoughYs = []

while True:
    _, img = cap.read()

    b, g, r = cv2.split(img)
    r = np.int16(r)
    b = np.int16(b)
    r_minus_b = r - b 
    r_minus_b = (r_minus_b + abs(r_minus_b)) / 2
    r_minus_b = np.uint8(r_minus_b)

    imgHough = img.copy()

    Hough_circle(r_minus_b, imgHough)
    cv2.imshow("R_Minus_B", r_minus_b)
    cv2.putText(imgHough, "({:0<2d}, {:0<2d})".format(Hough_x, Hough_y), (20, 30),
                cv2.FONT_HERSHEY_PLAIN, 1, (255, 100, 0), 2)

    cv2.imshow('Pingpong Position', imgHough)

    HoughXs.append(Hough_x)
    HoughYs.append(Hough_y)

    if cv2.waitKey(pulse_ms) & 0xFF == ord('q'):
        print("Quit\n")
        break

cap.release()
cv2.destroyAllWindows()

