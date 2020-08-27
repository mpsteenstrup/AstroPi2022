import ephem
from picamera import PiCamera
#import os
#dir_path = os.path.dirname(os.path.realpath(__file__))

name = "ISS (ZARYA)"
l1 = "1 25544U 98067A   19223.20985160  .00001115  00000-0  26628-4 0  9994"
l2 = "2 25544  51.6450  88.2760 0005764 242.1270 219.6998 15.51050586183792"
iss = ephem.readtle(name, l1, l2)

cam = PiCamera()
cam.resolution = (1296,972) # Valid resolution for V1 camera
iss.compute()

def get_latlon():
    iss.compute() # Get the lat/long values from ephem

    long_value = [float(i) for i in str(iss.sublong).split(":")]

    if long_value[0] < 0:

        long_value[0] = abs(long_value[0])
        cam.exif_tags['GPS.GPSLongitudeRef'] = "W"
    else:
        cam.exif_tags['GPS.GPSLongitudeRef'] = "E"
    cam.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/10' % (long_value[0], long_value[1], long_value[2]*10)

    lat_value = [float(i) for i in str(iss.sublat).split(":")]

    if lat_value[0] < 0:

        lat_value[0] = abs(lat_value[0])
        cam.exif_tags['GPS.GPSLatitudeRef'] = "S"
    else:
        cam.exif_tags['GPS.GPSLatitudeRef'] = "N"

    cam.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/10' % (lat_value[0], lat_value[1], lat_value[2]*10)
    print(str(lat_value), str(long_value))

get_latlon()

cam.capture('gps1.jpg')