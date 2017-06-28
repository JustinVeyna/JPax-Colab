'''
Created on Jun 23, 2017

@author: Justin Veyna
'''
import scrapy
from urllib.parse import urljoin
TEST = True

"""
IMPORTANT: To run use the below command:
    scrapy runspider JPAX_Crawler.py -o data_files/out.json
"""

from CrawlerConstants import START_URLS, CRAWLER_SETTINGS, get_character_from_url, IMAGE_CAP, PROGRESS_FILE
import SaveLoader as sl

class crawler(scrapy.Spider):
    name = "JPAX"
    start_urls = START_URLS
    custom_settings = CRAWLER_SETTINGS
    
    def parse(self, response):
        #store the files for different characters in different folders
        character = get_character_from_url(response.url)        
        img_count = 0
        for img_obj in response.xpath('//post'):#for each image
            if img_count > IMAGE_CAP:
                break
            #
            if is_single_char(img_obj):
                img_count+=1
                id = img_obj.xpath('@id').extract_first()#image id
                tmb = img_obj.xpath('@preview_url').extract_first()#thumbnail reletive link        
                u = urljoin(response.url, tmb) #url of thumbnail
                d = {'id': id, 'tumbnail': tmb, "character": character, 'image_urls': [u]}
                yield d #sends request to save info
        update_char_progress(character)

def update_char_progress(character):
    d = sl.pickle_load(PROGRESS_FILE)
    d[character] = (d[character] + 1)%11 #TODO: do I want the % ?
    sl.pickle_save(d, PROGRESS_FILE)

def is_single_char(img_object) -> bool:
    #only does check for girls for now
    img_tags = img_object.xpath('@tags').extract_first()
    return "1girl" in img_tags or "1boy" in img_tags

    

if __name__ == '__main__':
    if TEST:
        response = None
        with open('data_files/sample_files/GelbooruSamplePageMatsushima.xml', 'r') as f:
            response = scrapy.Selector(text = f.read())
        for img_obj in response.xpath('//post'):
                print({'id': img_obj.xpath('@id').extract_first(), 'tumbnail': img_obj.xpath('@preview_url').extract_first()})
