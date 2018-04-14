__author__ = "Neil"
__time__ = "2018/4/14 20:26"
#[[A1 A2 B1],[A3 A4 B2]]
# [[A1 A2],[A3 A4]]  [[B1],[B2]]
# newX = A1*x + A2*y+B1
# newY = A3*x +A4*y+B2
# x->x*0.5 y->y*0.5
# newX = 0.5*x
import cv2
import numpy as np
img = cv2.imread('1.png',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matScale = np.float32([[0.5,0,0],[0,0.5,0]])
dst = cv2.warpAffine(img,matScale,(int(width/2),int(height/2)))
cv2.imshow('dst',dst)
cv2.waitKey(0)