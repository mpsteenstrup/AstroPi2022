from sense_hat import SenseHat
import datetime
from time import sleep

s = SenseHat()
s.low_light = True

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds = 5)

with open ("vejrdata.csv", "w") as file:
    file.write("time , Temperature , Pressure, Humidity \n")

while now_time < start_time + duration:
    t = s.get_temperature()
    p = s.get_pressure()
    h = s.get_humidity()
    now_time = datetime.datetime.now()

with open ("Vejrrapport.csv", "a") as file:
    file.write("%s, %s C, %s Millibars, %s %%rH \n" % (now_time, t, p, h))
    sleep(0.1)

yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
nothing = (0,0,0)
grey = (169, 169, 169)
cyan = (240, 248, 255)

def sun():
    Y = yellow
    O = nothing
    logo = [
    O, O, O, O, Y, O, O, O,
    O, O, Y, O, Y, O, O, O,
    O, O, O, Y, Y, O, Y, O,
    Y, Y, Y, Y, Y, Y, O, O,
    O, O, Y, Y, Y, Y, Y, Y,
    O, Y, O, Y, Y, O, O, O,
    O, O, O, Y, O, Y, O, O,
    O, O, O, Y, O, O, O, O,
    ]
    return logo

def cloud():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, O, O, O,
    O, W, W, W, W, W, W, O,
    W, W, W, W, W, W, W, W,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def snowflake():
    C = cyan
    O = nothing
    logo = [
    O, O, O, O, C, O, O, O,
    O, O, O, C, C, C, O, O,
    O, C, O, O, C, O, O, O,
    C, C, C, C, C, O, C, O,
    O, C, O, C, C, C, C, C,
    O, O, O, C, O, O, C, O,
    O, O, C, C, C, O, O, O,
    O, O, O, C, O, O, O, O,
    ]
    return logo

def raincloud():
    B = blue
    G = grey
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, G, G, O, O,
    O, O, G, G, G, G, G, O,
    O, G, G, G, G, G, G, G,
    O, O, G, G, G, G, G, O,
    O, B, O, O, O, B, O, O,
    B, O, O, B, O, O, O, O,
    O, O, B, O, O, O, O, O,
    ]
    return logo

images = [sun, cloud, raincloud, snowflake]
count = 0

# Programmet viser nogle bestemte logoer, alt efter hvad temperaturen/luftfugtigheden er

while h > 90 & t > 5:
  s.set_pixels(images[2 % len(images)]())

while t > 18 & h < 90:
  s.set_pixels(images[0 % len(images)]())

while t < 18 & t > 5 & h < 90:
  s.set_pixels(images[1 % len(images)]())

while t < 5 & h < 90:
  s.set_pixels(images[3 % len(images)]())
