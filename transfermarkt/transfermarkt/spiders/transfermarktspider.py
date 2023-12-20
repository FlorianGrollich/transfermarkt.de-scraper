import scrapy


class TransfermarktsSpider(scrapy.Spider):
    name = "transfermarktspider"
    allowed_domains = ["transfermarkt.de"]
    start_urls = ["https://www.transfermarkt.de/spielbericht/index/spielbericht/4095985"]

    def parse(self, response):
        spieler = response.css('span.aufstellung-rueckennummer-name')
        endstand = response.css('div.sb-endstand::text').get()

        yield {'endstand': endstand}