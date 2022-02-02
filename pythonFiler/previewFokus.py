import time
import picamera

camera = picamera.PiCamera()

camera.start_preview()
time.sleep(1)
camera.stop_preview()
camera.close()
