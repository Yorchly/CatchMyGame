import logging
import re

from scrapper.common import CommonScrapper
from scrapper.settings import INSTANTGAMING_FILENAME
from scrapper.utils import formatting_price_2

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class InstantGamingScrapper(CommonScrapper):
    url = "https://www.instant-gaming.com/es/busquedas/?query={}"
    filename = INSTANTGAMING_FILENAME
    games_xpath = "//div[@class=' item mainshadow']"

    def __init__(self, game_name: str):
        self.url = self.url.format(game_name)

    def get_game(self, element):
        title = element.xpath(".//div[@class='name']/text()")
        price = element.xpath(".//div[@class='price']/text()")
        link = element.xpath(".//a[@class='cover']/@href")

        if title and price and link:
            return {
                "title": str(title[0]),
                "price": re.sub(r"[\s\\r\\nâ¬]", "", formatting_price_2(str(price[0]))),
                'link': str(link[0])
            }
        else:
            logger.error(
                "Xpath are not working properly in InstantGamingScrapper. Title, price or link cannot be obtained"
            )
            return {}
