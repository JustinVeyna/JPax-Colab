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

START_URLS = ["https://gelbooru.com/index.php?page=post&s=list&tags=matsushima_michiru"]



class crawler(scrapy.Spider):
    name = "JPAX"
    start_urls = START_URLS
    custom_settings = {
        'BOT_NAME': 'JPAX',
        'IMAGES_STORE':'mtsma',
        'ITEM_PIPELINES':{'scrapy.pipelines.images.ImagesPipeline': 1},
        'DOWNLOAD_DELAY':.5
    }
    
    def parse(self, response):
        for img_obj in response.css('span.thumb'):
            id = img_obj.css('span::attr(id)').extract_first()#image id
            tmb = img_obj.css('img::attr(src)').extract_first()#thumbnail reletive link
                        
            u = urljoin(response.url, tmb) #url of thumbnail
            i = {'image_urls': [u]}
            yield i #sends request to save thumbnail
            
            d = {'id': id, 'tumbnail': tmb}           
            yield d #sends request to save info

if __name__ == '__main__':
    if TEST: #will test link selection
        response = None
        with open('GelbooruSamplePageMatsushima', 'r') as f:
            response = scrapy.Selector(text = f.read())
        for img_obj in response.css('span.thumb'):
                print({'id': img_obj.css('span::attr(id)').extract(), 'tumbnail': img_obj.css('img::attr(src)').extract()})