import cv2
import numpy as np
import glob

#demo1_detect all
img_array = []
for filename in glob.glob('/Users/tia/Desktop/UE1_projet/runs/detect/exp/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('demo1.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release

#demo2_detect only ball
img_array = []
for filename in glob.glob('/Users/tia/Desktop/UE1_projet/runs/detect/exp1/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('demo2.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release

#demo3_detect using classes which including personne, racket and ball
img_array = []
for filename in glob.glob('/Users/tia/Desktop/UE1_projet/runs/detect/exp2/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('demo3.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release


