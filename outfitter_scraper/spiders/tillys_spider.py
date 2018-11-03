# -*- coding: utf-8 -*-

# Class responsible for crawling 'www.tillys.com' for image urls.

import re

from ..items import OutfitterScraperItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

   
class TillysSpider(CrawlSpider):
    name = 'tillys'
    start_urls = [
        'https://www.tillys.com/men/clothing/t-shirts/',
        'https://www.tillys.com/men/clothing/shorts/'
    ]
    rules = (
        Rule(LinkExtractor(
            restrict_css='.search-options-container .first-last > .page-next'),
            callback='parse_catalog_page', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_catalog_page(response)

    def parse_catalog_page(self, response):
        item = OutfitterScraperItem()
        
        clothing_match = re.search(r'clothing/(.+)/', response.url)
        if clothing_match:
            captured = clothing_match.group(1)
            clothing = {
                't-shirts': 'tops',
                'shorts': 'bottoms'
            }.get(captured, 'unknown')
            item['clothing'] = clothing

        item['image_names'] = []
        item['image_urls'] = []
        for image in response.css('.prod-thumb-image'):
            title = image.xpath('@title').extract_first()
            url = image.xpath('@data-yo-src').extract_first()
            if not url:
                url = image.xpath('@src').extract_first()      
            item['image_names'].append(title)
            item['image_urls'].append(url)

        return item