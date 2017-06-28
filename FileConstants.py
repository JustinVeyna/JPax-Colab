'''
Created on Jun 28, 2017

@author: Justin Veyna
'''
import os
import re

IMG_PATH = "imgs/full"
SORTED_IMG_PATH = "imgs/sorted"

def is_img(filename):
    return re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename)

def strip_file_type(filename, key = None):
    assert "/" not in filename
    filename.split(".")[0]
    d = {"name": filename.split(".")[0], "type":filename.split(".")[1]}
    if key==None:
        return d
    else:
        return d[key]
    

def all_img_files(key=None):
    for root, dirnames, filenames in os.walk(IMG_PATH):
            for filename in filenames:
                if is_img(filename):
                    path = os.path.join(root, filename)
                    d = {"root":root, "filename":filename, "path":path}
                    if key==None:
                        yield d
                    else:
                        yield d[key]