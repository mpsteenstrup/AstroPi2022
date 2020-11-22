import datetime
from time import sleep
import os
from sense_hat import SenseHat
sense = SenseHat()

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + '/test.csv'

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=30)

with open ("filename", "w") as file:
    file.write("time , Temperature, Humidity \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    h = sense.get_humidity()
    now_time= datetime.datetime.now()

    with open ("filename", "a") as file:
        file.write("%s, %s, %s  \n" % (now_time, t,h))
    sleep(2.5)

    if(t < 10):
        sense.show_message("Det er koldt", text_colour=[0, 0, 255], scroll_speed=0.05)

    elif(10 < t < 20):
        sense.show_message("Det er lunkent", text_colour=[0, 255, 0], scroll_speed=0.05)
    
    else:
        sense.show_message("Det er varmt", text_colour=[255, 0, 0], scroll_speed=0.05)

    if(h < 25):
        sense.show_message("laveste chance for regn", text_colour=[50, 50, 50], scroll_speed=0.05)
    
    elif(25 < h < 50):
        sense.show_message("lav chance for regn", text_colour=[50, 50, 100], scroll_speed=0.05)

    elif(50 < h < 75):
        sense.show_message("chance for regn", text_colour=[50, 50, 150], scroll_speed=0.05)

    elif(75 < h < 99):
        sense.show_message("høj chance for regn", text_colour=[50, 50, 200], scroll_speed=0.05)
    
    else:
        sense.show_message("Det regner", text_colour=[50, 50, 255], scroll_speed=0.05)
