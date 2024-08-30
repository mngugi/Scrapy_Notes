from pathlib import Path
from typing import Any, Iterable


import scrapy
from scrapy.http import Response


class twitterSpider( scrapy.Spider):
    name = "twitter"
    
    
    def start_requests(self):
        urls = [
            "https://x.com/home"
            
            
        ] 
        for url in urls:
            yield scrapy.Request( url=url, callback=self.parse)
            
            
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"twitter-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        
    
    