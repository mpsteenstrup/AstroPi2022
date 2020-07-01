import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('../billeder/blue.jpg')

#print(img.shape)
#img = img[80:1000,300:1600]



def find_ballon(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (90,50,50), (125,255,255))
    output = cv2.bitwise_and(img, img, mask=mask)
    return mask, output


mask, ballon = find_ballon(img)
print(mask[:20,:20])
print(mask[40:60,40:60])

cv2.imshow('image',img)
cv2.imshow('ballon',ballon)
cv2.imshow('mask',mask)
#cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
