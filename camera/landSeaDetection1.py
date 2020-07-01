import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('../billeder/blue.jpg')

#print(img.shape)
#img = img[80:1000,300:1600]



def find_border(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0,0,0), (180,255,45))
    output = cv2.bitwise_and(img, img, mask=mask)
    return output

def find_sea(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (90,50,50), (125,255,255))
    output = cv2.bitwise_and(img, img, mask=mask)
    return output

def find_cloud(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0,0,120), (180,30,255))
    output = cv2.bitwise_and(img, img, mask=mask)
    return output

def find_ground(img, border, sea, cloud):
    output = cv2.bitwise_xor(img, border)
    output = cv2.bitwise_xor(output, sea)
    output = cv2.bitwise_xor(output, cloud)
    return output


border = find_border(img)
sea = find_sea(img)
cloud = find_cloud(img)
ground = find_ground(img, border, sea, cloud)


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.namedWindow('sea',cv2.WINDOW_NORMAL)
cv2.namedWindow('border',cv2.WINDOW_NORMAL)
cv2.namedWindow('ground',cv2.WINDOW_NORMAL)

#cv2.imshow('mask',mask)
cv2.imshow('image',img)
cv2.imshow('sea',sea)
cv2.imshow('border',border)
cv2.imshow('ground',ground)

cv2.resizeWindow('image', 600,600)
cv2.resizeWindow('sea', 600,600)
cv2.resizeWindow('border', 600,600)
cv2.resizeWindow('ground', 600,600)
#cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
