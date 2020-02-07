# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AwsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    job_ID = scrapy.Field()
    posted = scrapy.Field()
    updated = scrapy.Field()
    info = scrapy.Field()
    description = scrapy.Field()
    basic = scrapy.Field()
    prefer = scrapy.Field()
    team = scrapy.Field()
    category = scrapy.Field()
