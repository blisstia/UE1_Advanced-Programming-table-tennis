# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:59:46 2021

@author: Chenyin WU
"""

##############################################################################
# Table tennis position detection under ideal conditions                     #
# Color tracking                                                             #
##############################################################################


import cv2
import numpy as np

def empty(a):
    pass

def draw_direction(img, lx, ly, nx, ny):
    dx = nx - lx
    dy = ny - ly
    if abs(dx) < 4 and abs(dy) < 4:
        dx = 0
        dy = 0
    else:
        r = (dx**2 + dy**2)**0.5
        dx = int(dx/r*40)
        dy = int(dy/r*40)
    cv2.arrowedLine(img, (60, 100), (60+dx, 100+dy), (0, 255, 0), 2)

frameWidth = 960
frameHeight = 544
cap = cv2.VideoCapture('/Users/tia/Desktop/UE1_projet/dataset/test/videos/Pingpong.mp4')
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 80) 
pulse_ms = 30

lower_ball = np.array([0, 140, 190])
upper_ball = np.array([32, 255, 255])

lower_table = np.array([0, 0, 80])
upper_table = np.array([255, 255, 255])

targetPos_x = 0
targetPos_y = 0
lastPos_x = 0
lastPos_y = 0
ColorXs = []
ColorYs = []

while True:
    _, img = cap.read()
    
    blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(imgHsv, lower_table, upper_table)
    res = cv2.bitwise_and(img, img, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cordinates = list()
    for c in contours:
        c = cv2.convexHull(c)
        area = cv2.contourArea(c)

        perimeter = cv2.arcLength(c, True)
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 4:
            if area > (img.shape[1] * img.shape[0]) / 440:
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                cv2.drawContours(img, [c], -1, (0, 255, 0), 3)
                cv2.putText(img, "Table", (cX - 20, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                for p in approx.tolist():
                    cordinates.append((p[0][0], p[0][1]))

    imgMask = cv2.inRange(imgHsv, lower_ball, upper_ball) 
    imgOutput = cv2.bitwise_and(img, img, mask=imgMask)
    contours, hierarchy = cv2.findContours(imgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    imgMask = cv2.cvtColor(imgMask, cv2.COLOR_GRAY2BGR)

    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5:
            x, y, w, h = cv2.boundingRect(cnt)
            lastPos_x = targetPos_x
            lastPos_y = targetPos_y
            targetPos_x = int(x+w/2)
            targetPos_y = int(y+h/2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(img, (targetPos_x, targetPos_y), 2, (0, 255, 0), 4)

    cv2.putText(img, "({:0<2d}, {:0<2d})".format(targetPos_x, targetPos_y), (20, 30),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    draw_direction(img, lastPos_x, lastPos_y, targetPos_x, targetPos_y)

    imgStack = np.hstack([img, imgOutput])
    cv2.imshow('Pingpong Position', imgStack)
    cv2.imshow("table", mask)
    cv2.waitKey(1)
    
    ColorXs.append(targetPos_x)
    ColorYs.append(targetPos_y)
    
    if cv2.waitKey(pulse_ms) & 0xFF == ord('q'):
        print("Quit\n")
        break

cap.release()
cv2.destroyAllWindows()