from sense_hat import SenseHat
sense = SenseHat()

def lowpass(n, axis):
    ax = ay = az = 0
    for i in range(n):
        acceleration= sense.get_accelerometer_raw()
        ax += acceleration[axis]
    return ax/n

def highpass(n, axis):
    ax = ay = az = 0
    for i in range(n):
        acceleration= sense.get_accelerometer_raw()
        ax += acceleration[axis]
    return acceleration[axis]-ax/n


while True:
    print(f"low pass filter: {lowpass(10,'x')}")
    print(f"high pass filter: {highpass(10,'x')}")
