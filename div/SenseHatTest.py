from sense_hat import SenseHat

sense = SenseHat()

t= sense.get_temperature()

print("t  = %s" % t)
sense.show_message("temperaturen er %s" % t)