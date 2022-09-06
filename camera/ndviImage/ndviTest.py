import cv2
import numpy as np
from fastiecm import fastiecm

original = cv2.imread('images/cslab3ogel_Files_RawData_raw_image_116.jpeg') # load image

def display(image, image_name):
    image = np.array(image, dtype=float)/float(255) #convert to an array
    shape = image.shape
    height = int(shape[0]/2)
    width = int(shape[1]/2)
    image = cv2.resize(image, (width,height))
    cv2.namedWindow(image_name) # create window
    cv2.imshow(image_name, image) # display image
    cv2.waitKey(0) # wait for key press
    cv2.destroyAllWindows()
    
def contrast_stretch(im):
    im_min = np.percentile(im, 5)
    im_max = np.percentile(im, 95)
    
    out_min = 0.0
    out_max = 255.0    
    out = im - im_min
    out *= (out_max-out_min)/(im_max-im_min)
    out += im_min
    return out

def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = r.astype(float) + b.astype(float)
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float)-r)/bottom
    return ndvi

#display(original,'park')
contrasted = contrast_stretch(original)
#display(contrasted, 'contrasted park')
#cv2.imwrite('contrasted.png', contrasted)
ndvi = calc_ndvi(contrasted)
ndvi_contrasted = contrast_stretch(ndvi)
#display(ndvi_contrasted,'NDVI')
cv2.imwrite('ndvi.png',ndvi)
color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
display(color_mapped_image, 'Color mapped')
cv2.imwrite('color_mapped_image.png', color_mapped_image)
mapped')

#cv2.imwrite('color_mapped_image.png', color_mapped_image)
#cv2.imwrite('original.png', original)

