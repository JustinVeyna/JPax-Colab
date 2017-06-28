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
from CrawlerConstants import CHARACTERS
import matplotlib.pyplot as plt
from numpy import uint8
from HashCharMap import get_hash_char_map
from FileConstants import all_img_files

DEBUG = False

RESIZE = (128,128)

def gen_classes(filename, hcm):
    try:
        chars = hcm[filename.split(".")[0]]
    except KeyError:
        print("KeyError:", filename.split(".")[0])
        chars = []
    return list(map(lambda x: x in chars, CHARACTERS))

def show_imgs(imgs):
    for img in imgs:
        plt.imshow(uint8(img))
        plt.show()

if __name__ == '__main__':
    print("Starting Preprocessing")
    hcm = get_hash_char_map()
    images = []
    image_classes = []
    for filename in all_img_files(key="path"):
        image = ndimage.imread(filepath, mode="RGB")
        image_resized = misc.imresize(image, RESIZE)
        images.append(image_resized)
        image_classes.append(gen_classes(filename, hcm))
        if DEBUG:
            show_imgs([image, image_resized])
                                                
    sl.pickle_save([images, image_classes], "data_files/imgs.dat")
