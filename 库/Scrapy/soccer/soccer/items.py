# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MatchItem(Item):
    country = Field()
    league = Field()
    date = Field()
    home_team = Field()
    away_team = Field()
    home_goals1 = Field()
    home_goals2 = Field()
    away_goals1 = Field()
    away_goals2 = Field()