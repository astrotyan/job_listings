# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AzureItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    job_id = scrapy.Field()
    date = scrapy.Field()
    travel = scrapy.Field()
    profession = scrapy.Field()
    role = scrapy.Field()
    employment = scrapy.Field()
    description = scrapy.Field()
    responsibilites = scrapy.Field()
    qualifications = scrapy.Field()
