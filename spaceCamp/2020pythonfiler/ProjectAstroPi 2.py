#LIBRARIES

from picamera import PiCamera
import picamera
import os
from time import sleep
from picamera import PiCamera, Color
import time
from PIL import Image
from datetime import datetime
from sense_hat import SenseHat


##################################

#INITATING

sense = SenseHat()
camera = PiCamera()
camera.resolution = (100, 100)

#################################

#Variables

Update = True
selection = False
mode = 'All'
catalog = 1

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
w = (255, 255, 255)
o = (255, 100, 0)
y = (255, 255, 0)
n = (0, 0, 0)


################################

while Update:

    while mode == 'All':
        t = sense.get_temperature()
        t = round(t,1)
        t = t - 12

        camera.exposure_mode = 'auto'
        camera.shutter_speed = camera.exposure_speed

        camera.capture('image.jpg')
        sleep(1)
        
        photo = Image.open('image.jpg')
        photo = photo.convert('RGB')

        width = photo.size[0]
        height = photo.size[1]
        lightlist = []
        for i in range(width*0.25,width*0.75):
            for j in range(height*0.25,width*0.75):
                RGB = photo.getpixel((i,j))
                R,G,B = RGB
                lightvalue = R + G + B
                lightvalue = lightvalue / 3
                lightvalue = lightvalue / 255
                lightvalue = lightvalue * 100
                lightlist.append(lightvalue)
        lightvalue = int(sum(lightlist)/len(lightlist))

        if lightvalue <= 5:
            status = "Very bad."
        if 5 < lightvalue < 10:
            status = "Bad."
        if 10 < lightvalue < 25:
            status = "Not optimal."
        if 25 < lightvalue < 50:
            status = "Maybe. Somewhat limited, but definitely possible."
        if 50 < lightvalue < 75:
            status = "Optimal. Most plants should be able to grow."
        if 75 < lightvalue < 100:
            status = "Optimal. Very high intensity, some plants can't grow."


        sense.clear()
        
        if lightvalue > 0:
            sense.set_pixel(3,7,(255,0,0))
        
        if lightvalue > 12:

            sense.set_pixel(3,6,(255,125,0))

        if lightvalue > 25:
            sense.set_pixel(3,5,(255,190,0))
        
        if lightvalue > 38:
            sense.set_pixel(3,4,(255,255,0))

        if lightvalue > 50:
            sense.set_pixel(3,3,(100,255,0))

        if lightvalue > 66:
            sense.set_pixel(3,2,(0,255,0))

        if lightvalue > 80:
            sense.set_pixel(3,1,(80,255,0))

        if lightvalue > 95:
            sense.set_pixel(3,0,(180,255,0))

        print("")
        print("Time: %s" % str(datetime.now().strftime('%H:%M:%S')))
        print("Raw Values: " + str(RGB))

        print("LightValue: " + str(round(lightvalue, 1)))
        print("Overall Status: " + status)

        os.remove("image.jpg")

        if t > 0:
            sense.set_pixel(0,7,(0,0,255))

        if t > 5:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))

        if t > 10:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))
            sense.set_pixel(0,5,(100,0,150))

        if t > 15:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))
            sense.set_pixel(0,5,(100,0,150))
            sense.set_pixel(0,4,(150,0,100))

        if t > 20:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))
            sense.set_pixel(0,5,(100,0,150))
            sense.set_pixel(0,4,(150,0,100))
            sense.set_pixel(0,3,(200,0,50))

        if t > 25:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))
            sense.set_pixel(0,5,(100,0,150))
            sense.set_pixel(0,4,(150,0,100))
            sense.set_pixel(0,3,(200,0,50))
            sense.set_pixel(0,2,(250,0,25))

        if t > 30:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))
            sense.set_pixel(0,5,(100,0,150))
            sense.set_pixel(0,4,(150,0,100))
            sense.set_pixel(0,3,(200,0,50))
            sense.set_pixel(0,2,(250,0,25))
            sense.set_pixel(0,1,(255,0,0))

        if t > 35:
            sense.set_pixel(0,7,(0,0,255))
            sense.set_pixel(0,6,(50,0,200))
            sense.set_pixel(0,5,(100,0,150))
            sense.set_pixel(0,4,(150,0,100))
            sense.set_pixel(0,3,(200,0,50))
            sense.set_pixel(0,2,(250,0,25))
            sense.set_pixel(0,1,(255,0,10))
            sense.set_pixel(0,0,(255,0,0))

        h = sense.get_humidity()
        h = round(h,1)
        
        if h > 0:
            sense.set_pixel(1,7,(0,0,100))

        if h > 12:
            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))

        if h > 25:
            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))
            sense.set_pixel(1,5,(0,0,150))

        if h > 37:
            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))
            sense.set_pixel(1,5,(0,0,150))
            sense.set_pixel(1,4,(0,0,175))

        if h > 50:
            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))
            sense.set_pixel(1,5,(0,0,150))
            sense.set_pixel(1,4,(0,0,175))
            sense.set_pixel(1,3,(0,0,200))

        if h > 62:
            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))
            sense.set_pixel(1,5,(0,0,150))
            sense.set_pixel(1,4,(0,0,175))
            sense.set_pixel(1,3,(0,0,200))
            sense.set_pixel(1,2,(0,0,225))
            
        if h > 75:

            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))
            sense.set_pixel(1,5,(0,0,150))
            sense.set_pixel(1,4,(0,0,175))
            sense.set_pixel(1,3,(0,0,200))
            sense.set_pixel(1,2,(0,0,225))
            sense.set_pixel(1,1,(0,0,255))

        if h > 97:
            sense.set_pixel(1,7,(0,0,100))
            sense.set_pixel(1,6,(0,0,125))
            sense.set_pixel(1,5,(0,0,150))
            sense.set_pixel(1,4,(0,0,175))
            sense.set_pixel(1,3,(0,0,200))
            sense.set_pixel(1,2,(0,0,225))
            sense.set_pixel(1,1,(0,0,240))
            sense.set_pixel(1,0,(0,0,255))

        p = sense.get_pressure()
        p = round(p,1)
        
        if p > 300:
            sense.set_pixel(2,7,(0,0,255))

        if p > 500:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))

        if p > 700:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))
            sense.set_pixel(2,5,(100,0,150))

        if p > 800:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))
            sense.set_pixel(2,5,(100,0,150))
            sense.set_pixel(2,4,(150,0,100))

        if p > 900:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))
            sense.set_pixel(2,5,(100,0,150))
            sense.set_pixel(2,4,(150,0,100))
            sense.set_pixel(2,3,(200,0,50))

        if p > 1000:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))
            sense.set_pixel(2,5,(100,0,150))
            sense.set_pixel(2,4,(150,0,100))
            sense.set_pixel(2,3,(200,0,50))
            sense.set_pixel(2,2,(250,0,25))

        if p > 1100:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))
            sense.set_pixel(2,5,(100,0,150))
            sense.set_pixel(2,4,(150,0,100))
            sense.set_pixel(2,3,(200,0,50))
            sense.set_pixel(2,2,(250,0,25))
            sense.set_pixel(2,1,(255,0,0))

        if p > 1200:
            sense.set_pixel(2,7,(0,0,255))
            sense.set_pixel(2,6,(50,0,200))
            sense.set_pixel(2,5,(100,0,150))
            sense.set_pixel(2,4,(150,0,100))
            sense.set_pixel(2,3,(200,0,50))
            sense.set_pixel(2,2,(250,0,25))
            sense.set_pixel(2,1,(255,0,10))
            sense.set_pixel(2,0,(255,0,0))


        sleep(1)
    
        #SAVE

        with open ("team_data.csv", "a") as file:
            file.write("Time: %s" % str(datetime.now()))
            file.write("\n")
            file.write("Pressure: %s" % p)
            file.write("\n")
            file.write("Humidity: %s" % h)
            file.write("\n")
            file.write("Temperature %s: " % t)
            file.write("\n")
            file.write("Lightintensity: %s" % str(round(lightvalue, 1)))
            file.write("\n")
            file.write("##########")
            file.write("\n")
            file.close()

        with open ("pres_data.csv", "a") as presfile:
            presfile.write("%s" % p)
            presfile.close()

        with open ("temp_data.csv", "a") as tempfile:
            tempfile.write("%s" % t)
            tempfile.close()

        with open ("humi_data.csv", "a") as humifile:
            humifile.write("%s" % h)
            humifile.close()

        with open ("ligh_data.csv", "a") as lighfile:
            lighfile.write("%s" % str(round(lightvalue, 1)))
            lighfile.close()

        sleep(2)

        overallstatus = 0

        #VERY GOOD SCORES
        
        if (50 < lightvalue < 75):
            overallstatus = overallstatus + 2

        if (1005 < p < 1025):
            overallstatus = overallstatus + 2

        if (80 < h < 100):
            overallstatus = overallstatus + 2

        if (15 < t < 20):
            overallstatus = overallstatus + 2

        # GOOD SCORES

        if (40 < lightvalue < 50):
            overallstatus = overallstatus + 1
            
        if (75 < lightvalue < 100):
            overallstatus = overallstatus + 1

        if (1005 < p < 1025):
            overallstatus = overallstatus + 1

        if (990 < p < 1005):
            overallstatus = overallstatus + 1

        if (70 < h < 80):
            overallstatus = overallstatus + 1

        if (12 < t < 15):
            overallstatus = overallstatus + 1

        if (20 < t < 23):
            overallstatus = overallstatus + 1

        print("Overall: %s" % overallstatus)
        print(t, h, p, lightvalue)

        very_good_smiley = [
            n, n, g, g, g, g, n, n,
            n, g, n, n, n, n, g, n,
            g, n, g, n, n, g, n, g,
            g, n, n, n, n, n, n, g,
            g, n, g, n, n, g, n, g,
            g, n, n, g, g, n, n, g,
            n, g, n, n, n, n, g, n,
            n, n, g, g, g, g, n, n,
        ]
        good_smiley = [
            n, n, y, y, y, y, n, n,
            n, y, n, n, n, n, y, n,
            y, n, y, n, n, y, n, y,
            y, n, n, n, n, n, n, y,
            y, n, n, n, n, y, n, y,
            y, n, y, y, y, n, n, y,
            n, y, n, n, n, n, y, n,
            n, n, y, y, y, y, n, n,
        ]
        bad_smiley = [
            n, n, o, o, o, o, n, n,
            n, o, n, n, n, n, o, n,
            o, n, o, n, n, o, n, o,
            o, n, n, n, n, n, n, o,
            o, n, o, o, o, o, n, o,
            o, n, n, n, n, n, n, o,
            n, o, n, n, n, n, o, n,
            n, n, o, o, o, o, n, n,
        ]
        very_bad_smiley = [
            n, n, r, r, r, r, n, n,
            n, r, n, n, n, n, r, n,
            r, n, r, n, n, r, n, r,
            r, n, n, n, n, n, n, r,
            r, n, n, r, r, n, n, r,
            r, n, r, n, n, r, n, r,
            n, r, n, n, n, n, r, n,
            n, n, r, r, r, r, n, n,
        ]


        if (6 <= overallstatus < 8):
            sense.set_pixels(very_good_smiley)

        if (4 <= overallstatus < 6):
            sense.set_pixels(good_smiley)

        if (2 <= overallstatus < 4):
            sense.set_pixels(bad_smiley)

        if (0 <= overallstatus < 2):
            sense.set_pixels(very_bad_smiley) 

"""
Kartoffel:
Lys = medium ~ høj
Tryk = 1013 mbar
Fugtighed = 80-95%
Temp = 15-20 Celsius


"""
######################################################################

camera.stop_preview()
print("Program ended.")

