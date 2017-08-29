import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
    name = 'test'


class MySpider2(scrapy.Spider):
    name = 'test2'

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

# process.crawl(MySpider)
# process.crawl(MySpider2)  # Run multiple spiders
# process.start()  # the script will block here until the crawling is finished


from scrapy.utils.project import get_project_settings

# process = CrawlerProcess(get_project_settings())

# 'test' is the name of one of the spiders of the project.
# process.crawl('test', domain='scrapinghub.com')
# process.start() # the script will block here until the crawling is finished
