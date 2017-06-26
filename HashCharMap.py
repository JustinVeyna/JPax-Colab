'''
Created on Jun 26, 2017

@author: Shintomo
'''
"""
IMPORTANT: Must modify the json file to make this work:
    1: replace "][" with "],["
    2: replace "]]" with "]" #to clean up past modifications
    3: make sure the file starts with "[["
    4: make sure the file ends with "]]"
TODO: Will eventually add this to the code...(prep_json_file)
"""

HASH_CHAR_FILE = "data_files/HashChar.p"

import json
import SaveLoader as sl
from pprint import pprint

def prep_json_file():
    with open('data_files/out.json') as data_file:
        pass #TODO: see above IMPORTANT

def process_json():
    d = dict()
    with open('data_files/out.json') as data_file:    
        data = json.load(data_file)
        for r in data:
            for item in r:
                if "images" in item.keys() and "checksum" in item["images"][0].keys():
                    d[item["images"][0]["checksum"]] = item["character"]
    sl.pickle_save(d, HASH_CHAR_FILE)

def get_hash_char_map():
    return sl.pickle_load(HASH_CHAR_FILE)

if __name__ == '__main__':
    process_json() 
        