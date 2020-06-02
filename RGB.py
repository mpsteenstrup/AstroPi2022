from PIL import Image
import numpy as np
#import PIL
im  = Image.open('billeder/land2.png')
rgb_im = im.convert('RGB')
imageW = im.size[0]
imageH = im.size[1]
rs=0
gs=0
bs=0
n = 0

for y in range(0, imageH):
    for x in range(0, imageW):
        r,g,b = rgb_im.getpixel((x,y))
        if r<150 and g<150 and r>50:
            n=n+1
            rs = r+rs
            gs = r+gs
            bs = b+bs

rs = rs/n
gs = gs/n
bs = bs/n

r,g,b = rgb_im.getpixel((10,10))

print(r,g,b)
print(rs,gs,bs)