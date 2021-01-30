import re

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from app.settings import STEAM_FILENAME
from scrapper.scrapper.spiders.common_spider import CommonSpider


class SteamSpider(CommonSpider):
    name = "steam"
    file_name = STEAM_FILENAME
    url = "https://store.steampowered.com/search/?term={}"
    games_xpath = "//div[@id='search_resultsRows']/a"

    @staticmethod
    def get_item(game):
        return {
            'title': game.xpath(".//span[@class='title']/text()").get(),
            'price': re.sub(r'[\s\\r\\n]', '',
                            game.xpath(".//div[@class='col search_price  responsive_secondrow']/text()").get()),
            'link': game.xpath("./@href").get()
        }


def initializing_steam_spider(game_name):
    process = CrawlerProcess(get_project_settings())

    process.crawl(SteamSpider, game=game_name)
    process.start()
