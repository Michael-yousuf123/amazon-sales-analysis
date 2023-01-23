import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['http://www.amazon.com/']

    def parse(self, response):
        author = response.css(".a-link-child ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text").extract()
        title = response.css(".a-link-normal ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text").extract()
        types = response.css(".a-text-normal::text").extract()
        price = response.css(".a-size-base , ._cDEzb_p13n-sc-price_3mJ9Z::text").extract()
        review = response.css(".a-link-normal .a-size-small::text").extract()
        rate = response.css(".a-link-normal .a-icon-alt::text").extract()
        year = ""
        
        pass