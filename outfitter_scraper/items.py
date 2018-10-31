# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from enum import Enum
import scrapy


class Clothing(Enum):
    UNKNOWN = 1
    T_SHIRTS = 2,
    SHORTS = 3,
    

class OutfitterScraperItem(scrapy.Item):
    # url of the page images were scraped from
    source_url = scrapy.Field()
    # the type of clothing depicted in the images
    clothing = scrapy.Field()
    # the urls of the images scraped
    img_urls = scrapy.Field()
