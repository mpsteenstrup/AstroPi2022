from sense_hat import SenseHat
import time

s = SenseHat()

temperatur = s.get_temperature()

print(temperatur)

with open("gemData.csv","w") as file:
  file.write("temperaturen er %s" % temperatur)
