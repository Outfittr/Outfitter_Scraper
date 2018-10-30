from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
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

    def parse_catalog_page(self, response):
        # extract clothing type from response url
        clothing_match = re.search(r'clothing/(.+)/', response.url)
        clothing = clothing_match.group(1) if clothing_match else 'unknown'

        # extract image urls
        selected_urls = response.css('.prod-thumb-image::attr(data-yo-src)')
        img_urls = selected_urls.extract()

        return {
            'clothing': clothing,
            'img_urls': img_urls
        }