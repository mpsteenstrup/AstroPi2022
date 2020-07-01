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




while (now_time < start_time + datetime.timedelta(minutes=1)):
    print("Doing stuff")
    sleep(1)


    dir_path = os.path.dirname(os.path.realpath(__file__))
#    print(dir_path)
    f= open(dir_path+"/data01.csv","a")

    print("capturing an image")
    filename='/image.jpg'
    path_and_filename = dir_path+filename
    camera.capture(path_and_filename)
    print("after image capture")
    img = cv2.imread(path_and_filename)
    nborder_pixel, nsea_pixel, ncloud_pixel, nground_pixel, total_img_pixel =global_classificator(img)
    now_time = datetime.datetime.now()
