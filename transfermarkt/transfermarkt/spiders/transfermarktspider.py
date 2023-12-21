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

    @staticmethod
    def _getStartingTeams(response):
        players = response.css('span.aufstellung-rueckennummer-name').css('a::attr(href)').getall()
        return players[:11:], players[11::]

    @staticmethod
    def _getBench(response):
        benchTeam1 = response.css('table.ersatzbank')[0].css('a::attr(href)').getall()
        benchTeam2 = response.css('table.ersatzbank')[1].css('a::attr(href)').getall()
        coachTeam1 = benchTeam1[-1]
        benchTeam1.pop(-1)
        coachTeam2 = benchTeam2[-1]
        benchTeam2.pop(-1)
        return benchTeam1, benchTeam2, coachTeam1, coachTeam2


    def parse(self, response, **kwargs):
        referee = response.xpath('/html/body/div[2]/main/div[1]/div/div/div[2]/div[2]/p[2]/a').css(
            "a::attr(href)").get()
        end_score = response.css('div.sb-endstand::text').get().strip()
        half_time_score = self._get_halftime_score(response)
        startingTeam1, startingTeam2 = self._getStartingTeams(response)
        benchT1, benchT2, coachT1, coachT2 = self._getBench(response)
        competition = response.css('a.direct-headline__link::attr(href)').get()
        stadium = response.css('span.hide-for-small').css('a::attr(href)').get()
        amountOfViewes =response.css('span.hide-for-small').css('strong::text)')

        return {
            "startingTeam1": startingTeam1,
            "startingTeam2": startingTeam2,
            "benchTeam1": benchT1,
            "benchTeam2": benchT2,
            "coachTeam1": coachT1,
            "coachTeam2": coachT2,
            "competition": competition,
            "stadium": stadium,
            "referee": referee,
            "endscore": end_score,
            "half_time_score": half_time_score
        }
