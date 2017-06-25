'''
Created on Jun 23, 2017

@author: Shintomo
'''
import scrapy

TEST = False

scrapy.IMAGES_STORE = '/mtsma'

#scrapy runspider quotes_spider.py -o results.json
START_URLS = ["https://gelbooru.com/index.php?page=post&s=list&tags=matsushima_michiru"]
class crawler(scrapy.Spider):
    name = "JPAX crawler"
    start_urls = START_URLS
    def parse(self, response):
        for img_obj in response.css('span.thumb'):
            d = {'id': img_obj.css('span::attr(id)').extract(), 'tumbnail': img_obj.css('img::attr(src)').extract()}
            
            yield d
            

if __name__ == '__main__':
    if TEST:
        response = None
        with open('GelbooruSamplePageMatsushima', 'r') as f:
            response = scrapy.Selector(text = f.read())
        for img_obj in response.css('span.thumb'):
                print({'id': img_obj.css('span::attr(id)').extract(), 'tumbnail': img_obj.css('img::attr(src)').extract()})