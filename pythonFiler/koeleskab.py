import datetime
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=4)

with open ("koeleskab.csv", "w") as file:
    file.write("time , Temperature , pressure \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    p = sense.get_pressure()
    now_time= datetime.datetime.now()
    print(now_time)
    with open ("koeleskab.csv", "a") as file:
        file.write("%s, %s, %s  \n" % (now_time, t,p))
    sleep(0.1)
