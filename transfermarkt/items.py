import scrapy


class MatchItem(scrapy.Item):
    startingTeam1 = scrapy.Field()
    benchTeam1 = scrapy.Field()
    coachTeam1 = scrapy.Field()
    endScoreTeam1 = scrapy.Field()
    halfScoreTeam1 = scrapy.Field()
    team1 = scrapy.Field()
    #placementTeam1 = scrapy.Field()

    startingTeam2 = scrapy.Field()
    benchTeam2 = scrapy.Field()
    coachTeam2 = scrapy.Field()
    endScoreTeam2 = scrapy.Field()
    halfScoreTeam2 = scrapy.Field()
    team2 = scrapy.Field()
    #placementTeam2 = scrapy.Field()

    referee = scrapy.Field()
    stadium = scrapy.Field()
    amountOfViewers = scrapy.Field()
    #date = scrapy.Field()
    #temperature = scrapy.Field()
    competition = scrapy.Field()
