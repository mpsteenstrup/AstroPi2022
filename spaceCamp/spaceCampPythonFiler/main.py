#This program is part of the project where we want to analyse patterns in the clouds
#at locations where we compare the cloud patterns with the predicted cloud patterns.
#One of the motivations for this is the growing knowledge about the fact that as the temperature gradient
#between the north pole and the equator is influenced by climate change, the wind and therefor cloud patterns are influenced.

#Fore this purpose we will take down high resolutions images with clouds and metadata (time and location), wich is what this program is to do


#Labraries neede are collected via importings
import ephem
#from picamera import PiCamera
import numpy as np
import cv2
import datetime
#import sys
import os
from ephem import readtle, degree
from PIL import Image
from pathlib import Path
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep


name = "ISS (ZARYA)" #thes three lines sets up variables for finding the position of the ISS
line1 = "1 25544U 98067A   21042.30870520  .00003041  00000-0  63421-4 0  9992"
line2 = "2 25544  51.6440 245.3345 0002839 359.6306 175.5159 15.48962705269087"

iss = ephem.readtle(name, line1, line2)#For when it is later calculated where the ISS is, initally the position object variables are sat up. 

dir_path = Path(__file__).parent.resolve()#the path to where this porgam sits on the ISS astro pi is found and sat up in a varaiable.
start_time = datetime.datetime.now()#timing variables are sat up here 
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=10780)#Here the time limit is sat up just under the max of thre hours (3*3600-20)
disc_use=0
disc_use_limit=2980000000#Here the limit is sat up so that it keeps just under the the guidline rules of max 3GB-20 MB (2980 000 000B)
imagenumber=1 #this numbering system gets its initial value for image name numbering



#Here the border of the image is found so that pixels that are not showing the earth can be disregarded when estimating percentage.
def find_border(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0,0,0), (180,255,45))
    output = cv2.bitwise_and(img, img, mask=mask)
    return output


#Here the sea pixels are found using a threshold range estimated from earlier images from ISS
def find_sea(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#converts image from BGR
    mask = cv2.inRange(hsv, (90,50,50), (125,255,255))#sorts pixel that are within the range and returns a black and white image.
    output = cv2.bitwise_and(img, img, mask=mask)#returnere billede der viser pixel der har værdi inden for tærskel område, alle andre pixel er sorte.
    return output

#Here the cloud pixels are found using a threshold range estimated from earlier images from ISS
def find_cloud(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0,0,120), (180,30,255))
    output = cv2.bitwise_and(img, img, mask=mask)
    return output

#Here the the pixels of land is found since it is not cloud,sea and border pixels
def find_ground(img, border, sea, cloud):
    output = cv2.bitwise_xor(img, border)
    output = cv2.bitwise_xor(output, sea)
    output = cv2.bitwise_xor(output, cloud)
    return output

#Here the number of pixels in the category is found later to be used for calculate percentage
def compute_percentage(masked_img):
    single_band_img= masked_img[:,:,0]>0
    npixel_class = sum(sum(1*single_band_img))
    return npixel_class


#Here the percantage is calculated using the fact that not all image pixels are from earth
def calculate_percentage(border_output,cloud_output):
    nborder_pixel = compute_percentage(border_output)
    #nsea_pixel = compute_percentage(sea_output)
    ncloud_pixel = compute_percentage(cloud_output)
    #nground_pixel = compute_percentage(ground_output)
    total_img_pixel = img[:,:,0].shape[0]*img[:,:,0].shape[1]
    #return [nborder_pixel/total_img_pixel, nsea_pixel/(total_img_pixel-nborder_pixel), ncloud_pixel/total_img_pixel, nground_pixel/total_img_pixel]
    #here in the return line the number of pixels border pixels subtracted in the is from an estimate from same resolution image analysed with the border_output,
    #in order to make the program robust a number is used asuming that the Astro pi camera is still situated at the same position.
    return ncloud_pixel/(total_img_pixel-1321839.0)


#the image is categorized in a class and saved with metadata in it and size used on disc is noticed and returned:
def global_classificator(img,imagenumber):
    #print("tiden før det starter med billedbahandlingen",datetime.datetime.now())
    border_output = find_border(img)
    #sea_output = find_sea(img)
    cloud_output = find_cloud(img)#Here we get the image containing coudpixels 
    #ground_output = find_ground(img, border_output, sea_output, cloud_output)
    percentage_cloud=float(calculate_percentage(border_output,cloud_output))#here the percentage of cloud pixels is found.
    #print("tiden lige efter billedanalysen",datetime.datetime.now())

    if percentage_cloud > 0.25:
        #print('Cloudimage')
        image_filelocation_and_name = f"{dir_path}/Image%04d.tif"%imagenumber#the the path of the program and imagename both set in variable.
        cv2.imwrite(image_filelocation_and_name, cloud_output)#The image file is saved in tif format because tif has metadata and is lossless.  
        imagenumber=imagenumber+1#the numbering used for naming is updated

        #print("Her er strlse af billede efter det gemmes")
        #print("tiden lige efter billedet er gemt",datetime.datetime.now())
        imgageToBeTagged = Image.open(image_filelocation_and_name)#the image file is opened så that metadata can bewritten to the tags
        # convert the latitude and longitude to EXIF-appropriate representations
        south, exif_latitude = convert(iss.sublat)#gps longitude data i converted til exif format
        west, exif_longitude = convert(iss.sublong)#gps longitude data i converted til exif format
        imgageToBeTagged.tag[37000]=exif_latitude#Here the gps coordianates are saved in the standard exif format
        imgageToBeTagged.tag[37001] = "S" if south else "N"#Here the gps coordianates are saved in the standard exif format
        imgageToBeTagged.tag[37002]=exif_longitude#Here the gps coordianates are saved in the standard exif format
        imgageToBeTagged.tag[37003]= "W" if west else "E"#Here the gps coordianates are saved in the standard exif format
        imgageToBeTagged.tag[37004]= str(iss.sublat / degree)+","+str(iss.sublong / degree)#get the spherical coordinates saved in a googlefriendly format.
        imgageToBeTagged.tag[37005]=str(now_time)#Here the time and date is saved 
        imgageToBeTagged.save(image_filelocation_and_name, tiffinfo=imgageToBeTagged.tag) #The log data is written to the metadata tag in tif image format
        b = os.path.getsize(image_filelocation_and_name)
        #print(b)
        #print("tiden lige efter billedet er blevet åbnet igen og skrevet til i metadata",datetime.datetime.now())
        return b,imagenumber
    b = 0
    return b,imagenumber


def convert(angle):
    """
    Convert an ephem angle (degrees, minutes, seconds) to
    an EXIF-appropriate representation (rationals)
    e.g. '51:35:19.7' to '51/1,35/1,197/10'
    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    degrees, minutes, seconds = (float(field) for field in str(angle).split(":"))
    exif_angle = f'{abs(degrees):.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return degrees < 0, exif_angle


def takepicture():
    with PiCamera() as camera:
        camera.resolution = (2592,1944)
        rawCapture = PiRGBArray(camera)
        # giver kameraet tid til at indstille sig
        sleep(1)
        iss.compute()
        now_time= datetime.datetime.now()
        #print("billedet er taget ",now_time,"ved positionen",str(iss.sublat / degree)+","+str(iss.sublong / degree))
        camera.capture(rawCapture, format='bgr') # bemærk at vi gemmer som blå, grøn, rød
        img = rawCapture.array
    return img,now_time


#Here the program runs as long as it is within the time- and sizelimits
while (now_time < start_time + duration)&(disc_use<disc_use_limit):
    #
    #From here and until the conditional statement the position of the iss and the sun is calculated 
    #
    iss.compute()
    sun = ephem.Sun()
    sun.compute()

    # Angle is translated to radian numbers with repr 
    ## below is the equatorial angle between the sun and iss 
    vinkelra = float(repr(iss.ra))-float(repr(sun.ra))

    # Angle is translated to radian numbers with repr 
    ## below is the vertical angle between the sun and iss 
    
    lower_thresholdra= 3.14/2 #-1.024983
    upper_thresholdra= 3*3.14/2
    lower_thresholddec= 3.14/2 #-1.024983
    upper_thresholddec= 3*3.14/2
    # conditioned on how the iss sun angle is the the imagetaking and processing is done. 
    if (upper_thresholdra > abs(vinkelra) > lower_thresholdra):#&(upper_thresholddec > abs(vinkeldec) > lower_thresholddec):
        now_time=datetime.datetime.now()
        #Here it is dark so no other processing is done.        
        
    else:
        #is is light so the processing is done
        img,now_time=takepicture()#image is obtained its updated ('now_time') time and position is noted but not saved
        b,imagenumber=global_classificator(img,imagenumber)#desired image is saved with log data in it.
        disc_use=disc_use+b#the size of disc use is updated
                
    
    #print(indegrees)
    #interval = now_time - start_time
    #print("teoretisk pladsforbrug",disc_use,"og tiden der er gået er ",interval.total_seconds(),"og tiden er nu",now_time)
    
#print("og grænsen for diskplads er",disc_use_limit)

data_file = dir_path/"loggfile.csv"

with open (data_file, "w") as file:
    file.write("starttime, endtime, number of images \n")
    file.write("%s, %s, %s  \n" % (start_time, now_time,imagenumber-1))




# at sætte programmet ind til kun at gemme når det er sky billede --- er gjort skal lige rette tærskel
#ændre navnet til main
