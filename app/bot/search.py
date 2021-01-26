import logging

import requests

from app.models.game import Game
from app.settings import SEARCH_URL

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def search_game(game_name, web):
    response = requests.get(SEARCH_URL + "{}+{}".format(game_name, web))
    game = None

    if response.status_code != 200:
        logger.error("Error getting data from request")
    else:
        items = response.json().get("items")
        if items:
            first_item = items[0]
            game = Game(
                name=f"{game_name} en {web}",
                price=first_item.get("pagemap").get("offer")[0].get("price") if first_item.get("pagemap").get(
                    "offer") else "No se ha podido obtener",
                currency=first_item.get("pagemap").get("offer")[0].get("pricecurrency") if first_item.get("pagemap").get(
                    "offer") else "No se ha podido obtener",
                link=first_item.get("link")
            )

    return game
