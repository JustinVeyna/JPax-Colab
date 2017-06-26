'''
Created on Jun 25, 2017

@author: Shintomo
'''
from urllib.parse import parse_qs
from collections import defaultdict
import ProgressLoader as PL

IMAGE_CAP=200

CRAWLER_SETTINGS = {
        'BOT_NAME': 'JPAX',
        'IMAGES_STORE':'imgs\\',
        'ITEM_PIPELINES':{'scrapy.pipelines.images.ImagesPipeline': 1},
        'DOWNLOAD_DELAY':.5
    }

START_URLS = []
START_URLS_OLD = []

PROGRESS_FILE = "SavedProgress.p"

characters = ["matsushima_michiru", "kousaka_kirino"]

hosts = [
    "gelbooru.com",
    "safebooru.org"
    ]
host = hosts[1]


base_url = "https://"+host+"/index.php?page=dapi&s=post&q=index&tags="
base_url_old = "https://"+host+"/index.php?page=post&s=list&tags="

char_dict = PL.load_progress_from_file()

if char_dict != None:
    for character in characters:
        START_URLS.append(base_url+character+"&pid="+str(char_dict[character]))
        START_URLS_OLD.append(base_url_old+character+"&pid="+str(char_dict[character]))
        

def get_character_from_url(url):
    return parse_qs(url)["tags"][0]
def get_PID_from_url(url):
    return parse_qs(url)["pid"][0]

#initialize if not created
#if initialized, make sure start url includes PID
#if not exist, initialize each char to 0
#if file exists, load dictionary informations, append PID from dictionary
#to the URL

