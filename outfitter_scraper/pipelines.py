# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes


class DefaultValuesPipeline(object):
    def process_item(self, item, spider):
        item.setdefault('clothing', 'unknown')
        return item


class StoreImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_item in item['image_items']:
            request = scrapy.Request(image_item['url'])
            request.meta['title'] = image_item['title']
            request.meta['clothing'] = item['clothing']
            yield request
    
    def file_path(self, request, response=None, info=None):
        hash = lambda x: hashlib.sha1(to_bytes(x)).hexdigest()
        return '{}/{}.jpg'.format(
            request.meta['clothing'], 
            hash(request.meta['title']))
