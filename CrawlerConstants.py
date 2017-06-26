'''
Created on Jun 25, 2017

@author: Shintomo
'''
from urllib.parse import parse_qs

IMAGE_CAP=200

CRAWLER_SETTINGS = {
        'BOT_NAME': 'JPAX',
        'IMAGES_STORE':'imgs\\',
        'ITEM_PIPELINES':{'scrapy.pipelines.images.ImagesPipeline': 1},
        'DOWNLOAD_DELAY':.5
    }

START_URLS = []
START_URLS_OLD = []


characters = ["matsushima_michiru", "kousaka_kirino"]

base_url = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags="
base_url_old = "https://gelbooru.com/index.php?page=post&s=list&tags="

for character in characters:
    START_URLS.append(base_url+character)
    START_URLS_OLD.append(base_url_old+character)
    
def get_character_from_url(url):
    return parse_qs(url)["tags"][0]