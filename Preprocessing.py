'''
Created on Jun 25, 2017

@author: Justin Veyna
'''
'''
Checklist
resize    X
rotate    
flip      
stretch???

'''

import os
from scipy import ndimage, misc
import SaveLoader as sl
import re
from CrawlerConstants import CHARACTERS, extract_chars
from time import sleep
import matplotlib.pyplot as plt
from numpy import uint8
from HashCharMap import get_hash_char_map

TEST = False
DEBUG = False

RESIZE = (128,128)

def gen_classes(filename, hcm):
    chars = hcm[filename]
    return list(map(lambda x: x in chars, CHARACTERS))

def show_imgs(imgs):
    for img in imgs:
        plt.imshow(uint8(img))
        plt.show()

if __name__ == '__main__':
    if TEST:
        for root, dirnames, filenames in os.walk("imgs/full"):
            print(root)
            for filename in filenames:
                if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                    filepath = os.path.join(root, filename)
                    print(filepath)
    else:
        hcm = get_hash_char_map()
        images = []
        image_classes = []
        for root, dirnames, filenames in os.walk("imgs/full"):
            for filename in filenames:
                if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
                    filepath = os.path.join(root, filename)
                    image = ndimage.imread(filepath, mode="RGB")
                    image_resized = misc.imresize(image, RESIZE)
                    images.append(image_resized)
                    image_classes.append(gen_classes(filename, hcm))
                    if DEBUG:
                        show_imgs([image, image_resized])
                                                
        sl.pickle_save([images, image_classes], "data_files/imgs.dat")
