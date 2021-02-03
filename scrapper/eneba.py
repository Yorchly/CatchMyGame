import logging

from scrapper.common import CommonScrapper
from scrapper.settings import ENEBA_FILENAME
from scrapper.utils import formatting_price

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class EnebaScrapper(CommonScrapper):
    url = "https://www.eneba.com/es/store/all?text={}&sortBy=RELEVANCE_DESC"
    filename = ENEBA_FILENAME
    games_xpath = "//div[@class='_2rxjGA _3nGiQg']"

    def __init__(self, game_name: str):
        self.url = self.url.format(game_name)

    def get_game(self, element):
        title = element.xpath(".//div[@class='_1ZwRcm']/span/text()")
        price = element.xpath(".//span[@class='_3RZkEb']/text()")
        link = element.xpath(".//a[@class='O0r4B8 qGNWom']/@href")

        if title and price and link:
            return {
                "title": str(title[0]),
                "price": formatting_price(str(price[0])),
                'link': "https://www.eneba.com{}".format(link[0])
            }
        else:
            logger.error("Xpath are not working properly in EnebaScrapper. Title, price or link cannot be obtained")
            return {}
