# -*- coding: utf-8 -*-

# Class responsible for crawling 'www.tillys.com' for image urls.

import re

from ..items import OutfittrScraperItem

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
        item = OutfittrScraperItem()
        
        # determine the type of clothing shown on the page
        clothing_match = re.search(r'clothing/(.+)/', response.url)
        if clothing_match:
            captured = clothing_match.group(1)         
            item['clothing'] = {
                't-shirts': 'tops',
                'shorts': 'bottoms'
            }.get(captured, 'unknown')

        # parse attributes from each image
        item['image_items'] = []
        for thumb in response.css('.prod-thumb-image'):        
            title = thumb.xpath('@title')
            url = thumb.xpath('@data-yo-src')
            if not url:
                url = thumb.xpath('@src')
            item['image_items'].append({
                'title': title.extract_first(),
                'url': url.extract_first()
            })

        return item