'''
Created on Jun 23, 2017

@author: Shintomo
'''
import scrapy
from urllib.parse import urljoin
TEST = False

"""
IMPORTANT: To run use the below command:
    scrapy runspider JPAX_Crawler.py -o results.json
"""

from CrawlerConstants import START_URLS, CRAWLER_SETTINGS, get_character_from_url, IMAGE_CAP, get_PID_from_url, PROGRESS_FILE
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
            img_count+=1
            id = img_obj.xpath('@id').extract_first()#image id
            tmb = img_obj.xpath('@preview_url').extract_first()#thumbnail reletive link
                        
            u = urljoin(response.url, tmb) #url of thumbnail
            i = {'image_urls': [u]}
            yield i #sends request to save thumbnail
            
            d = {'id': id, 'tumbnail': tmb, "character": character}
            yield d #sends request to save info
        update_char_progress(character)

def update_char_progress(character):
    d = sl.pickle_load(PROGRESS_FILE)
    d[character]+=1
    sl.pickle_save(d, PROGRESS_FILE)

if __name__ == '__main__':
    if TEST:
        response = None
        with open('GelbooruSamplePageMatsushima.xml', 'r') as f:
            response = scrapy.Selector(text = f.read())
        for img_obj in response.xpath('//post'):
                print({'id': img_obj.xpath('@id').extract_first(), 'tumbnail': img_obj.xpath('@preview_url').extract_first()})