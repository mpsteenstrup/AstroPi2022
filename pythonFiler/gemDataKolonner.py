import datetime
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=20)

with open ("test.csv", "w") as file:
    file.write("time , Temperature , pressure \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    p = sense.get_pressure()
    now_time= datetime.datetime.now()

    with open ("test.csv", "a") as file:
        file.write("%s, %s, %s  \n" % (now_time, t,p))
    sleep(1)
