from sense_hat import SenseHat
sense = SenseHat()
import math

def microtesla(x,y,z):
    math.sqrt((x*x)+(y*y)+(z*z))

o=(255,130,0)
b=(0,150,255)
h=(80,80,80)
g=(0,255,0)
gu=(255,255,0)

vaad = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, h, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]

toer = [
  b, b, g, g, b, b, b, b,
  b, b, g, g, b, g, b, b,
  g, b, g, g, b, g, b, b,
  g, b, g, g, b, g, b, b,
  g, g, g, g, g, g, b, b,
  b, b, g, g, b, b, b, b,
  gu, gu, gu, gu, gu, gu, gu, gu,
  gu, gu, gu, gu, gu, gu, gu, gu,
]

#Her finder vi temperaturen og printer det
temp = sense.temperature
sense.show_message("Temperaturen er")
sense.show_message(str(temp))

humid = sense.humidity
if humid >= 40:
    sense.show_message("Luffugtigheden er tør")
    sense.set_pixels(toer)
else:
    sense.show_message("Luffugtigheden er fugtig")
    sense.set_pixels(vaad)
sense.clear

while True:
    raw = sense.get_compass_raw()
    x = raw["x"]
    y = raw["y"]
    z = raw["z"]
    microtesla(x,y,z)
sense.show_message("Magnet feltet er",)
sense.show_message(microtesla(x,y,z))
sense.show_message("microtesla")