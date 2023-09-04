import scrapy


class TransfermarktspiderSpider(scrapy.Spider):
    name = "transfermarktspider"
    allowed_domains = ["transfermarkt.de"]
    start_urls = ["https://transfermarkt.de"]

    def parse(self, response):
        pass
