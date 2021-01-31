import logging
import re

from scrapper.common import CommonScrapper
from scrapper.settings import STEAM_FILENAME
from scrapper.utils import formatting_price

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class SteamScrapper(CommonScrapper):
    url = "https://store.steampowered.com/search/?term={}"
    filename = STEAM_FILENAME
    games_xpath = "//div[@id='search_resultsRows']/a"

    def __init__(self, game_name: str):
        self.url = self.url.format(game_name)

    def get_game(self, element):
        title = element.xpath(".//span[@class='title']/text()")
        price = element.xpath(".//div[@class='col search_price  responsive_secondrow']/text()")
        link = element.xpath("./@href")

        if title and price and link:
            return {
                "title": str(title[0]),
                "price": re.sub(r'[\s\\r\\n]', '', formatting_price(str(price[0]))),
                'link': str(link[0])
            }
        else:
            logger.error("Xpath are not working properly in SteamScrapper. Title, price or link cannot be obtained")
            return {}

