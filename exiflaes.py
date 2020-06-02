import PIL.ExifTags
import PIL.Image
img = PIL.Image.open('billeder/hav3.jpg')
exif_data = img._getexif()

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

#print(exif)
print('Brightness', exif['BrightnessValue'])

