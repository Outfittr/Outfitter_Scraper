# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import Clothing


class DefaultValuesPipeline(object):
    def process_item(self, item, spider):
        item.setdefault('clothing', Clothing.UNKNOWN)
        item.setdefault('img_urls', [])
        return item
