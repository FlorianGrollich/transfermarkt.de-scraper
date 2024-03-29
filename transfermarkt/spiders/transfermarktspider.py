import scrapy
import re

from transfermarkt.items import MatchItem
from transfermarkt.utils.utils import getNumberAllNumsFromStr


class TransfermarktSpider(scrapy.Spider):
    name = "transfermarktspider"
    allowed_domains = ["transfermarkt.de"]
    start_urls = ["https://www.transfermarkt.de/spielbericht/index/spielbericht/1"]

    @staticmethod
    def _get_halftime_score(response):
        f = getNumberAllNumsFromStr(response.css('div.sb-halbzeit span::text').get())
        s = getNumberAllNumsFromStr(response.css('div.sb-halbzeit::text')[1].get())
        return f, s

    @staticmethod
    def _getEndScore(response):
        score = response.css('div.sb-endstand::text').get().strip().split(":")
        return score[0], score[1]

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

    @staticmethod
    def _amountOfViews(response):
        return getNumberAllNumsFromStr(response.css('span.hide-for-small').css('strong::text').get())

    def extract_match_data(self, response):
        team1 = response.css('div.sb-heim').css('a::attr(href)').get()
        team2 = response.css('div.sb-gast').css('a::attr(href)').get()
        referee = response.xpath('/html/body/div[2]/main/div[1]/div/div/div[2]/div[2]/p[2]/a').css(
            "a::attr(href)").get()
        endScoreT1, endScoreT2 = self._getEndScore(response)
        halfTimeScoreT1, halfTimeScoreT2 = self._get_halftime_score(response)
        startingTeam1, startingTeam2 = self._getStartingTeams(response)
        benchT1, benchT2, coachT1, coachT2 = self._getBench(response)
        competition = response.css('a.direct-headline__link::attr(href)').get()
        stadium = response.css('span.hide-for-small').css('a::attr(href)').get()
        amountOfViews = self._amountOfViews(response)

        return {
            "team1": team1,
            "team2": team2,
            "startingTeam1": startingTeam1,
            "startingTeam2": startingTeam2,
            "benchTeam1": benchT1,
            "benchTeam2": benchT2,
            "coachTeam1": coachT1,
            "coachTeam2": coachT2,
            "halfScoreTeam1": int(halfTimeScoreT1),
            "halfScoreTeam2": int(halfTimeScoreT2),
            "endScoreTeam1": int(endScoreT1),
            "endScoreTeam2": int(endScoreT2),
            "referee": referee,
            "stadium": stadium,
            "amountOfViewers": int(amountOfViews),
            "competition": competition,
        }

    def parse(self, response, **kwargs):
        data = self.extract_match_data(response)
        item = MatchItem(**data)
        yield item
        next_match_id = self.get_next_match_id(response.url)
        if next_match_id is not None:
            next_url = f"https://www.transfermarkt.de/spielbericht/index/spielbericht/{next_match_id}"
            yield scrapy.Request(next_url, callback=self.parse)

    def get_next_match_id(self, current_url):
        current_id = int(current_url.split('/')[-1])
        next_id = current_id + 1

        if next_id > 10:
            return None

        return next_id