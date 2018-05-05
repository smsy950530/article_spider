# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PandaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PandaItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
    follow_count = scrapy.Field()
    num = scrapy.Field()
    room_id = scrapy.Field()
    html_url = scrapy.Field()
    has_id = scrapy.Field()

    pass
