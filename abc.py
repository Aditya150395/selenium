import scrapy
from scrapy_selenium import SeleniumRequest




class AbcSpider(scrapy.Spider):
    name = 'aditya' 
    

    def start_requests(self):
        yield SeleniumRequest(url='https://quotes.toscrape.com/page/1/', callback=self.parse_result)

    def parse_result(self, response):
        product = response.xpath("//div[@class='quote']")
        for i in product:
            title = i.xpath(".//span[@class='text']/text()").get()
            author = i.xpath(".//small[@class='author']/text()").get()
            yield{
                'name':title,
                'author': author
            }
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse_result)
