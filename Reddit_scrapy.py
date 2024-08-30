from typing import Any
import scrapy
from scrapy.http import Response

from reddit import RedditItem 

class RedditJobSpider(scrapy.Spider):
    
    name = 'reddit_job'
    
    
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/animals_and_pets/']
    
    
    def parse(self, response):
        #return super().parse(response, **kwargs)
    
        titles = response.css("a.title::text").extract()
        hrefs = response.css("a.title::attr(href)").extract()
        scores =  response.css("div.score.unnoted::attr(title)").extract()
        
        for item in zip(titles, hrefs, scores):
            new_item = RedditItem()
            
            new_item['title'] = item[0]
            new_item['href'] = item[1]
            new_item['score'] = item[2]
            
            yield new_item
        
    