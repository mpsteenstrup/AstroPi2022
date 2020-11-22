from sense_hat import SenseHat
from time import sleep
from time import asctime

sense = SenseHat()

temp = round(sense.get_temperature())
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())

message = 'Temperature is %d C Humidity is %d percent Pressure is %d mbars' %(temp,humidity,pressure)

sense.show_message(message, scroll_speed=(0.1),text_colour=[255,255,255], back_colour= [0,0,0])

for i in range(10):
  log = open("weather.txt","a")
  now = str(asctime())
  log.write(now + " " + message + "\n")
  print(message)
  sleep(5)
  
log.close()