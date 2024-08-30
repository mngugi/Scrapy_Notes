import scrapy
from scrapy.http import Response

class RedditJobSpider(scrapy.Spider):
    name = 'reddit_job'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/animals/']

    def parse(self, response: Response):
        # Extracting the titles of the posts
        titles = response.css("h3._eYtD2XCVieq6emjKBH3m::text").extract()
        
        # Extracting the links to the posts
        links = response.css("a.SQnoC3ObvgnGjWt90zD9Z::attr(href)").extract()
        
        # Extracting the score of the posts
        scores = response.css("div._1rZYMD_4xY3gRcSS3p8ODO::text").extract()

        for title, link, score in zip(titles, links, scores):
            yield {
                'title': title,
                'link': f'https://www.reddit.com{link}',
                'score': score
            }
