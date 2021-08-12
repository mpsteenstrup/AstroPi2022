import datetime
from pathlib import Path
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=180)

dir_path = Path(__file__).parent.resolve()
print(dir_path)
with open (str(dir_path)+"/test_path.csv", "w") as file:
    file.write("time , temperature , pressure \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    p = sense.get_pressure()
    now_time= datetime.datetime.now()

    with open (str(dir_path)+"/test_path.csv", "a") as file:
        file.write("%s, %s, %s  \n" % (now_time, t,p))
    sleep(0.1)
