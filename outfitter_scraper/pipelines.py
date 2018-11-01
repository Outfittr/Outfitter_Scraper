# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes


class DefaultValuesPipeline(object):
    def process_item(self, item, spider):
        item.setdefault('clothing', 'unknown')
        return item


class StoreImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            request = scrapy.Request(image_url)
            request.meta['clothing'] = item['clothing']
            yield request
    
    def file_path(self, request, response=None, info=None):
        filename = hashlib.sha1(to_bytes(request.url)).hexdigest()
        subdir = request.meta['clothing']
        return '{}/{}.jpg'.format(subdir, filename)
