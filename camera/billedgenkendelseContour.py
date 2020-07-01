import numpy as np
import cv2

im = cv2.imread('../billeder/blue.jpg')
imCopy = im.copy()
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (90,50,50), (125,255,255))
cv2.imshow('mask',mask)

contours, hierarchy =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imCopy,contours,-1,(0,0,255))
cv2.imshow('draw contours',imCopy)
cv2.waitKey(0)
