import numpy as np
import cv2

img = cv2.imread('../billeder/coast.jpg')

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

def compute_percentage(masked_img):
    single_band_img= masked_img[:,:,0]>0
    npixel_class = sum(sum(1*single_band_img))
    return npixel_class

def vis_billed(img,name):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name,img)
    cv2.resizeWindow(name, 600,600)

def calculate_percentage(border_output,sea_output,cloud_output,ground_output):
    nborder_pixel = compute_percentage(border_output)
    nsea_pixel = compute_percentage(sea_output)
    ncloud_pixel = compute_percentage(cloud_output)
    nground_pixel = compute_percentage(ground_output)
    total_img_pixel = img[:,:,0].shape[0]*img[:,:,0].shape[1]
    return [nborder_pixel/total_img_pixel, nsea_pixel/total_img_pixel, ncloud_pixel/total_img_pixel, nground_pixel/total_img_pixel]

def global_classificator(img):
    border_output = find_border(img)
    sea_output = find_sea(img)
    cloud_output = find_cloud(img)
    ground_output = find_ground(img, border_output, sea_output, cloud_output)

    vis_billed(border_output,'border')
    vis_billed(sea_output,'sea')
    vis_billed(cloud_output,'cloud')
    vis_billed(ground_output,'ground')
    print('border, sea, cloud, ground')
    print(calculate_percentage(border_output,sea_output,cloud_output,ground_output))

global_classificator(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
