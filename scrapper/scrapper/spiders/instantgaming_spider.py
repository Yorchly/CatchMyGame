from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app.settings import INSTANTGAMING_FILENAME
from scrapper.scrapper.spiders.common_spider import CommonSpider


class InstantGamingSpider(CommonSpider):
    name = "instantgaming"
    file_name = INSTANTGAMING_FILENAME
    url = "https://www.instant-gaming.com/es/busquedas/?query={}"
    games_xpath = "//div[@class=' item mainshadow']"

    @staticmethod
    def get_item(game):
        return {
            'title': game.xpath(".//div[@class='name']/text()").get(),
            'price': game.xpath(".//div[@class='price']/text()").get(),
            'link':  game.xpath(".//a[@class='cover']/@href").get()
        }


def initializing_instantgaming_spider(game_name):
    process = CrawlerProcess(get_project_settings())

    process.crawl(InstantGamingSpider, game=game_name)
    process.start()
