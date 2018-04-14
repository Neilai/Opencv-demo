__author__ = "Neil"
__time__ = "2018/4/14 19:54"
import cv2
# img = cv2.imread('1.png',1)
# print(img[0][0])
import numpy as np
img = cv2.imread('1.png',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(height/2)
dstWidth = int(width/2)
dstImage = np.zeros((dstHeight,dstWidth,3),np.uint8)#0-255
for i in range(0,dstHeight):#行
    for j in range(0,dstWidth):#列
        iNew = int(i*(height*1.0/dstHeight))
        jNew = int(j*(width*1.0/dstWidth))
        dstImage[i,j] = img[iNew,jNew]
cv2.imshow('dst',dstImage)
cv2.waitKey(0)