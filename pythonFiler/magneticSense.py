import datetime
from pathlib import Path
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=60*60*24)

dir_path = Path(__file__).parent.resolve()
print(dir_path)
with open (str(dir_path)+"/magneticSense.csv", "w") as file:
    file.write("time, x, y, z \n")

while now_time < start_time + duration:


    magneticfield = sense.get_compass_raw()

    x = magneticfield['x']
    y = magneticfield['y']
    z = magneticfield['z']

    now_time= datetime.datetime.now()

    with open (str(dir_path)+"/magneticSense.csv", "a") as file:
        file.write("%s, %s, %s, %s  \n" % (now_time, x, y, z))
    sense.show_message('running')
    print('running: ' + str(now_time))
    sleep(10)
sense.clear()
