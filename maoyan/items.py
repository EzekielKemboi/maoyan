# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    name=scrapy.Field()
    ename=scrapy.Field()
    #more=scrapy.Field()
    movietype=scrapy.Field()
    location=scrapy.Field()
    movietime=scrapy.Field()
    maidenshow=scrapy.Field()
    content=scrapy.Field()
    director=scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
