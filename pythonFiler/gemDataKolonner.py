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

with open (filename, "w") as file:
    file.write("time , Temperature , pressure \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    p = sense.get_pressure()
    now_time= datetime.datetime.now()

    with open (filename, "a") as file:
        file.write("%s, %s, %s  \n" % (now_time, t,p))
    sleep(1)
