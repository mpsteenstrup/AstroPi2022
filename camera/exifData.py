import ephem
from picamera import PiCamera
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

name = "ISS (ZARYA)"

l1 = "1 25544U 98067A   20160.44333333  .00000486  00000-0  16765-4 0  9992"
l2 = "2 25544  51.6452  31.7465 0002473  30.7477 336.6319 15.49429119230668"
iss = ephem.readtle(name, l1, l2)

cam = PiCamera()
cam.resolution = (3280,2464) # Valid resolution for V2 camera
iss.compute()

print('long: ',iss.sublong)
print('lat: ',iss.sublat)

def get_latlon():
    iss.compute() # Get the lat/long values from ephem

    long_value = [float(i) for i in str(iss.sublong).split(":")]

    if long_value[0] < 0:

        long_value[0] = abs(long_value[0])
        cam.exif_tags['GPS.GPSLongitudeRef'] = "West"
    else:
        cam.exif_tags['GPS.GPSLongitudeRef'] = "East"

    cam.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/10' % (long_value[0], long_value[1], long_value[2]*10)

    lat_value = [float(i) for i in str(iss.sublat).split(":")]

    if lat_value[0] < 0:

        lat_value[0] = abs(lat_value[0])
        cam.exif_tags['GPS.GPSLatitudeRef'] = "South"
    else:
        cam.exif_tags['GPS.GPSLatitudeRef'] = "North"

    cam.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/10' % (lat_value[0], lat_value[1], lat_value[2]*10)
    print(str(lat_value), str(long_value))

get_latlon()

cam.capture(dir_path+"/gps1.jpg")

import PIL.Image
img = PIL.Image.open('gps1.jpg')
exif_data = img._getexif()

print(exif_data)
