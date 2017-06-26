'''
Created on Jun 25, 2017

@author: Justin Veyna
'''

from urllib.parse import parse_qs
from CrawlerConstants import START_URLS

if __name__ == '__main__':
    print(START_URLS)
    print(parse_qs('https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=matsushima_michiru')["tags"])