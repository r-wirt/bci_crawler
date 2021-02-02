# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BciProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
    authors = scrapy.Field()
    publisher = scrapy.Field()
    journal = scrapy.Field()
    datepublished = scrapy.Field()
    source_link = scrapy.Field()
    isopenaccess = scrapy.Field()
