'''
Created on Jun 25, 2017

@author: Shintomo
'''

from urllib.parse import parse_qs

if __name__ == '__main__':
    print(parse_qs('https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=matsushima_michiru')["tags"])