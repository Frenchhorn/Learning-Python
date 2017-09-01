# -*- coding: utf-8 -*-
import scrapy

from soccer.items import MatchItem


class StatFootballSpider(scrapy.Spider):
    name = "match"
    start_urls = (
        'http://www.stat-football.com/en/',
    )

    def parse(self, response):
        for country in response.css("ul#menuA > li:not(.f11.t0.tar) > a::attr(href)").extract():
            yield response.follow(country, self.country)

    def country(self, response):
        for team in response.css('#tb01 .nw.s10.tal a::attr(href)').extract():
            yield response.follow(team, self.team)

    def team(self, response):
        title = response.css('title::text').extract_first()
        
