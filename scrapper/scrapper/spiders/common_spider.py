import json

import scrapy


class CommonSpider(scrapy.Spider):
    name = "common_spider"
    file_name = ""
    url = ""
    games_xpath = ""
    max_items = 3

    def start_requests(self):
        url = self.url
        game = getattr(self, 'game', None)

        yield scrapy.Request(url.format(game), self.parse)

    def parse(self, response, **kwargs):
        file = open(self.file_name, "w")
        count = 0

        for game in response.xpath(self.games_xpath):
            if count < self.max_items:
                item = self.get_item(game)
                count += 1
                file.write(f"{json.dumps(item)}\n")
            else:
                break

        file.close()

    @staticmethod
    def get_item(game):
        """
        You need to override this method in child class
        :param game:
        :return:
        """
        pass
