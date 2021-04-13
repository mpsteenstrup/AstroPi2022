# Thingspeak
Data med temperatur og luftfugtighed Thingspeak [https://thingspeak.com/channels/1350495](https://thingspeak.com/channels/1350495).
Programmet som kører på vores RPI ```humTempThingspeak.py```

```
from time import sleep
import Adafruit_DHT
import urllib3

sensor = Adafruit_DHT.DHT11
pin = 17
myAPI = '3P4FSZ66KPHJ6Z4S'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
http = urllib3.PoolManager()

print('starting')
while True:
    try:
        humi, temp = Adafruit_DHT.read_retry(sensor, pin)
        print(humi)
        print(temp)
        if isinstance(humi, float) and isinstance(temp, float) and humi<101:
            http.request("POST", baseURL+ '&field1=%s&field2=%s' % (temp, humi))
            print('sending')
    except:
        print('something went wrong')
        exit(0)
```

Programet er kopieret med scp gennem remote.it,
``` scp -P 32543 pi@proxy50.rt3.io:/home/pi/weatherstation/humTempThingspeak.py /Users/mpsteenstrup/AstroPi ```
