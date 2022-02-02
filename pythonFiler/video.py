import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    print("starter optagelse")
    camera.start_recording('my_video.h264')
    camera.wait_recording(10)
    print("optagelse slut")
    camera.stop_recording()
