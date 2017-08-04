# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    # Name of this spider
    name = "redditbot"
    # An optional list of strings containing domains that this spider is allowed to crawl
    allowed_domains = ["www.reddit.com/r/gameofthrones/"]
    start_urls = (
        'http://www.reddit.com/r/gameofthrones//',
    )

    def parse(self, response):
        """This function is called whenever the crawler successfully crawls a URL
        """
        # Extracting the context using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()
        
        # Give the extracted content row-wise
        for item in zip(titles, votes, times, comments):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'vote': item[1],
                'time': item[2],
                'comment': item[3],
            }
            
            # yield or give the scraped info to scrapy
            yield scraped_info