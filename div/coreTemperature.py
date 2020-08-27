import os
import time

while True:
	print(os.popen('vcgencmd measure_temp').readline())
	time.sleep(1)

