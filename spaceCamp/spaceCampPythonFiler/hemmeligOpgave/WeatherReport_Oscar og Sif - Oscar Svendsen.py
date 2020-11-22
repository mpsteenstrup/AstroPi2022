from sense_hat import SenseHat
sense = SenseHat()


t = sense.get_temperature()
t_corrected = round(t - 8)
t_corrected = str("Temperatur: %s C" %t)

p_før = round(sense.get_pressure(),1)
if p_før>1020:
    p = str("Tryk: %s millibar -> Højtryk, Solskin" %p_før)
if p_før<1006:
    p = str("Tryk: %s millibar -> Lavtryk, mulighed for regn" %p_før)
p = str("Tryk: %s millibar -> Omskifteligt" %p_før)

h_før = round(sense.get_humidity(),1)
if h_før<30:
    h = str("Luftfugtighed: %s %%rH -> Tørt" %h_før)
if h_før>50:
    h = str("Luftfugtighed: %s %%rH -> Fugtigt" %h_før)
h = str("Luftfugtighed: %s %%rH -> Behageligt" %h_før)


#sense.show_message("%s, %s, %s" %(t,h,p))
y = (255, 255, 0)   # yellow
n = (255, 128, 128) # pink
b = (0, 0, 255)     # blue
sense.show_message("%s" %t_corrected, text_colour=y)
sense.show_message("%s" %h, text_colour=b)
sense.show_message("%s" %p, text_colour=n)
