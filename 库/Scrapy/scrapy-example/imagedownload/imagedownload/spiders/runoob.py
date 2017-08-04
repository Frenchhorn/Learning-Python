# -*- coding: utf-8 -*-
import scrapy


class RunoobSpider(scrapy.Spider):
    name = "runoob"
    allowed_domains = ["www.runoob.com"]
    start_urls = (
        'http://www.runoob.com/',
    )
    custom_settings = {
        'IMAGES_STORE' : 'temp/images/'
    }

    def parse(self, response):
        img = response.css('img::attr(src)').extract()
        for item in img:
            scraped_info = {}
            if item.startswith('//'):
                # This is the field that scrapy checks for the image’s link
                scraped_info['image_urls'] = ['https:' + item]
                yield scraped_info
