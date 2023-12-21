import scrapy


class TransfermarktSpider(scrapy.Spider):
    name = "transfermarktspider"
    allowed_domains = ["transfermarkt.de"]
    start_urls = ["https://www.transfermarkt.de/spielbericht/index/spielbericht/4095985"]

    @staticmethod
    def _get_halftime_score(response):
        f = response.css('div.sb-halbzeit span::text').get()
        s = response.css('div.sb-halbzeit::text')[1].get()
        return f + s


    def parse(self, response):
        spieler = response.css('span.aufstellung-rueckennummer-name').css('a::attr(href)')
        ref = response.xpath('/html/body/div[2]/main/div[1]/div/div/div[2]/div[2]/p[2]/a').css("a::attr(href)")
        end_score = response.css('div.sb-endstand::text').get().strip()
        half_time_score = self._get_halftime_score(response)

        return {}
