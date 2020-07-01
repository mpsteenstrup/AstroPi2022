import datetime
from time import sleep
from picamera import PiCamera
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
#from skimage import img_as_float
import pandas as pd
import logging
import logzero
from logzero import logger
from sense_hat import SenseHat

sense = SenseHat()


# create a datetime variable to store the start time
start_time = datetime.datetime.now()
# create a datetime variable to store the current time
# (these will be almost the same at the start)
now_time = datetime.datetime.now()
print("tempo iniziale", start_time)
# Apro cattura immagini
camera = PiCamera()
camera.resolution = (1296,972)
# run a loop for 2 minutes

# formatting logfile csv
formatter = logging.Formatter('%(levelname)s, %(message)s');
logzero.formatter(formatter)


def write_line_on_csv(dir_path, val1, val2, val3, val4, val5):
    logzero.logfile(dir_path+"/data01.csv")
    print("writing logging csv file data01.csv")
    logzero.logger.info("%s, %s, %s, %s, %s", val1, val2, val3, val4, val5 )


def display_on_sensehat(stringa1, val1):
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    #sense.show_message("Astro Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)
    sense.show_message(stringa1, text_colour=yellow, back_colour=blue, scroll_speed=0.05)
    sleep(1)
    sense.show_message(str(val1), text_colour=yellow, back_colour=blue, scroll_speed=0.05)
    sleep(2)
    sense.clear()


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


def global_classificator(img):
    border_output = find_border(img)
    sea_output = find_sea(img)
    cloud_output = find_cloud(img)

    ground_output = find_ground(img, border_output, sea_output, cloud_output)
    nborder_pixel = compute_percentage(border_output)
    nsea_pixel = compute_percentage(sea_output)
    ncloud_pixel = compute_percentage(cloud_output)
    nground_pixel = compute_percentage(ground_output)
    total_img_pixel = img[:,:,0].shape[0]*img[:,:,0].shape[1]
    return [nborder_pixel, nsea_pixel, ncloud_pixel, nground_pixel, total_img_pixel]


counter = 0

while (now_time < start_time + datetime.timedelta(minutes=3)):
    print("Doing stuff")
    sleep(1)


    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    f= open(dir_path+"/data01.csv","a")


    #camera.start_preview()
    # Camera warm-up time
    #sleep(2)
    print("capturing an image")
    filename='/image.jpg'
    path_and_filename = dir_path+filename
    camera.capture(path_and_filename)
    print("after image capture")
    img = cv2.imread(path_and_filename)
    nborder_pixel, nsea_pixel, ncloud_pixel, nground_pixel, total_img_pixel =global_classificator(img)
    print(" writing of csv file data01.csv")
    write_line_on_csv(dir_path,nborder_pixel, nsea_pixel, ncloud_pixel, nground_pixel, total_img_pixel)

    #write_line_on_csv(dir_path,npixel_i,pixel_totali)

    #scrivo sul senshat
    sea_percentual= round((nsea_pixel/(1.0*(total_img_pixel)))*100)
    border_percentual= round((nborder_pixel/(1.0*(total_img_pixel)))*100)

    print("sea_percentual", sea_percentual)
    display_on_sensehat('S% ',sea_percentual)
    sleep(1)
    display_on_sensehat('B% ',border_percentual)

    if (counter%10)==0:
        print("saving on cvs files ",counter )
        f.write('saving image number = '+str(counter)+'\n')
        image_rescaled = img[0:-1:4,0:-1:4,2]#rescale(bandR, 1.0 / 4.0, anti_aliasing=False)
        imgDataFrame= pd.DataFrame(image_rescaled)
        imgDataFrame.to_csv(dir_path+"/data01.csv",mode='a', index=False)
        f.write('saved image number = '+str(counter)+'\n')

    #rimuovo immagine
    os.remove(dir_path+'/image.jpg')
    # update the current time
    now_time = datetime.datetime.now()
    print("tempo attuale", now_time, " delta_tempo", datetime.timedelta(minutes=2))
    counter = counter+1
    print("counter = ", counter)

f.close()
sense.clear()
