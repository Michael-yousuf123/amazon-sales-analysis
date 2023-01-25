import scrapy
from books.items import BooksItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/gp/bestsellers/2019/books/ref=zg_bsar_pg_1/ref=zg_bsar_pg_1?ie=UTF8&pg=1']
    def parse(self, response):


        author = response.css(".a-link-child ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text").extract()
        title = response.css(".a-link-normal ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text").extract()
        types = response.css(".a-text-normal::text").extract()
        price = response.css(".a-size-base , ._cDEzb_p13n-sc-price_3mJ9Z::text").extract()
        review = response.css(".a-link-normal .a-size-small::text").extract()
        rate = response.css(".a-link-normal .a-icon-alt::text").extract()
        
        count = 0

        for item in zip(author, title, types, price, review, rate):

            scraped_data = {
                'author': item[0],
                'title': item[1],
                'types': item[2],
                'price': item[3],
                'review': item[4],
                'rate': item[5],
            }
            yield scraped_data
        next_page = response.css('.a-normal a ::attr(href)').extract_first()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse)