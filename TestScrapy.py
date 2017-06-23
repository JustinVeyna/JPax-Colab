'''
Created on Jun 23, 2017

@author: Shintomo
'''
import scrapy
#scrapy runspider quotes_spider.py -o results.json
START_URLS = ["https://gelbooru.com/index.php?page=post&s=list&tags=matsushima_michiru"]
class crawler(scrapy.Spider):
    def __init__(self):
        pass
    def parse(self, response):
        pass
            

if __name__ == '__main__':
    response = None
    with open('GelbooruSamplePageMatsushima', 'r') as f:
        response = scrapy.Selector(f.read())
    for img_obj in respose.css('span.thumb'):
            yield {'id': img_obj.css('::attr(id)')}