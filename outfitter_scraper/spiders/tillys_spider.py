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
            item['clothing'] = {
                't-shirts': 'tops',
                'shorts': 'bottoms'
            }.get(captured)

        item['image_urls'] = response \
            .css('.prod-thumb-image::attr(data-yo-src)') \
            .extract()

        return item