import logging
import os

import requests
from lxml import etree

from scrapper.settings import REFERER, HTML_DIR
from scrapper.utils import get_random_ua

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class CommonScrapper:
    url = ""
    headers = {
        "user-agent": get_random_ua(),
        "referer": REFERER,
        'Content-Type': 'text/html',
    }
    max_count = 1
    # Filename where html code obtained from requests will be saved.
    filename = ""
    # Games list obtained with xpath.
    games_xpath = ""

    def get_content(self, elements: int =0):
        elements = elements if elements > 0 else self.max_count
        count = 0
        games = []
        logger.info("Getting response for {}".format(self.url))
        response = requests.get(self.url, headers=self.headers, timeout=5)
        if response.status_code == 200:
            logger.info("Response obtained for {} successfully".format(self.url))
            html = response.text
            html_location = os.path.join(HTML_DIR, self.filename)

            with open(html_location, "w", encoding="utf-8") as file:
                file.write(html)

            tree = etree.parse(html_location, etree.HTMLParser())

            for element in tree.xpath(self.games_xpath):
                if count < elements:
                    games.append(self.get_game(element))
                    count += 1
                else:
                    break

        logger.info("Games obtained for {} -> {}".format(self.url, games))
        return games

    def get_game(self, element):
        """
        You have to override this function in order to get games info
        :param element:
        :return:
        """
        pass
