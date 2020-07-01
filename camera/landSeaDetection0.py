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
