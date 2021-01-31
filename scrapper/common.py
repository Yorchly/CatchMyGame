import os

import requests
from lxml import etree
from lxml.etree import _Element

from scrapper.settings import REFERER, HTML_DIR
from scrapper.utils import get_random_ua


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
        response = requests.get(self.url, headers=self.headers)
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

        return games

    def get_game(self, element: _Element):
        """
        You have to override this functin in order to get games info
        :param element:
        :return:
        """
        pass
