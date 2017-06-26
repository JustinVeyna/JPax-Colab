'''
Created on Jun 25, 2017

@author: Shintomo
'''
'''
Checklist
resize
rotate
flip
stretch?????

'''
'''
import os
from scipy import ndimage, misc

images = []
for root, dirnames, filenames in os.walk("/imgs/full"):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            filepath = os.path.join(root, filename)
            image = ndimage.imread(filepath, mode="RGB")
            image_resized = misc.imresize(image, (64, 64))
            images.append(image_resized)
'''


if __name__ == '__main__':
    pass