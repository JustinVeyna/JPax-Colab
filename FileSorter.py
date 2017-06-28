'''
Created on Jun 28, 2017

@author: Justin Veyna
'''
from CrawlerConstants import CHARACTERS
from FileConstants import all_img_files, strip_file_type, SORTED_IMG_PATH
from HashCharMap import get_hash_char_map
from shutil import copyfile
import os

def gen_new_file_loc(filename, hcm):
    d = strip_file_type(filename)
    character = hcm[d["name"]][0]
    return os.path.join(SORTED_IMG_PATH, character, filename)

def sort_imgs():
    premake_dirs()
    hcm = get_hash_char_map()
    for file_d in all_img_files():
        try:
            new_path = gen_new_file_loc(file_d["filename"], hcm)
            copyfile(file_d["path"], new_path)
        except KeyError:
            print("KeyError")

def premake_dirs():
    if not os.path.exists(SORTED_IMG_PATH):
        os.mkdir(SORTED_IMG_PATH)
    for character in CHARACTERS:
        p = os.path.join(SORTED_IMG_PATH, character)
        if not os.path.exists(p):
            os.mkdir(p)
    
if __name__ == '__main__':
    sort_imgs()
        