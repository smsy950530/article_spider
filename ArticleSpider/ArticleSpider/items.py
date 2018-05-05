# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
import datetime
import time
from scrapy.loader import processors
from scrapy.loader import ItemLoader
from scrapy.exporters import JsonItemExporter


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItemLoader(ItemLoader):
    default_output_processor = processors.TakeFirst()


def del_str(value):
    value_num = re.match('(\d*).*', value).group(1)
    if value_num:
        value_num = int(value_num)
    else:
        value_num = 0
    return value_num


def set_date(value):

    value = value[0].strip().replace("·", " ").strip()
    try:
        date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        date = datetime.datetime.now().date()

    return date


def return_value(value):
    return value


class Artcilespidertest(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field(
        input_processor =processors.MapCompose(set_date)
    )
    tag = scrapy.Field(
        output_processor =processors.Join(",")
    )
    zan_num = scrapy.Field(
        input_processor =processors.MapCompose(del_str)
    )
    shoucang_num = scrapy.Field(
        input_processor =processors.MapCompose(del_str)
    )
    pinglun_num = scrapy.Field(
        input_processor =processors.MapCompose(del_str)
    )
    content = scrapy.Field()
    html_url = scrapy.Field()
    image_url = scrapy.Field(
        output_processor =processors.MapCompose(return_value)
    )
    article_id = scrapy.Field()


class LagouItemLoader(ItemLoader):
    default_output_processor = processors.TakeFirst()


class LagouItem(scrapy.Item):
    title = scrapy.Field()
    job_desc = scrapy.Field()
    job_need = scrapy.Field()
    job_tag = scrapy.Field()
    company_name = scrapy.Field()
    company_addr = scrapy.Field()
    crawl_time = scrapy.Field()
    url_object_id = scrapy.Field()


