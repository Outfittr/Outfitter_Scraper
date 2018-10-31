# -*- coding: utf-8 -*-

# Class responsible for crawling 'www.tillys.com' for image urls.

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import OutfitterScraperItem, Clothing
import re

        
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
        
        item['source_url'] = response.url

        clothing_match = re.search(r'clothing/(.+)/', response.url)
        if clothing_match:
            captured = clothing_match.group(1)
            item['clothing'] = {
                'shorts': Clothing.SHORTS,
                't-shirts': Clothing.T_SHIRTS
            }.get(captured, Clothing.UNKNOWN)

        selected_urls = response.css('.prod-thumb-image::attr(data-yo-src)')
        item['img_urls'] = selected_urls.extract()

        return item