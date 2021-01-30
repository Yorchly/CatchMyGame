from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app.settings import ENEBA_FILENAME
from scrapper.scrapper.spiders.common_spider import CommonSpider


class EnebaSpider(CommonSpider):
    name = "eneba"
    file_name = ENEBA_FILENAME
    url = "https://www.eneba.com/es/marketplace?text={}&sortBy=RELEVANCE_DESC"
    games_xpath = "//div[@class='_2rxjGA _3nGiQg']"

    @staticmethod
    def get_item(game):
        return {
            'title': game.xpath(".//div[@class='_1ZwRcm']/span/text()").get(),
            'price': game.xpath(".//span[@class='_3RZkEb']/text()").get(),
            'link': "https://www.eneba.com{}".format(
                game.xpath(".//a[@class='O0r4B8 qGNWom']/@href").get()
            )
        }


def initializing_eneba_spider(game_name):
    process = CrawlerProcess(get_project_settings())

    process.crawl(EnebaSpider, game=game_name)
    process.start()
