import time

from app.models.game import Game
from scrapper.eneba import EnebaScrapper
from scrapper.instantgaming import InstantGamingScrapper
from scrapper.steam import SteamScrapper
from scrapper.utils import get_random_delay


def get_games_results(game_name: str, web: str = "all"):
    """
    Get games results from spiders
    :param game_name:
    :param web:
    :return: list of games, obtained from spiders.
    """
    games = []
    not_formatted_games = []
    time.sleep(get_random_delay())
    if web == "eneba":
        not_formatted_games.extend(EnebaScrapper(game_name).get_content())
    elif web == "instantgaming":
        not_formatted_games.extend(InstantGamingScrapper(game_name).get_content())
    elif web == "steam":
        not_formatted_games.extend(SteamScrapper(game_name).get_content())
    elif web == "all":
        not_formatted_games.extend(EnebaScrapper(game_name).get_content())
        time.sleep(get_random_delay())
        not_formatted_games.extend(InstantGamingScrapper(game_name).get_content())
        time.sleep(get_random_delay())
        not_formatted_games.extend(SteamScrapper(game_name).get_content())

    for game in not_formatted_games:
        if game:
            games.append(
                Game(
                    title=game.get("title"),
                    price=game.get("price"),
                    link=game.get("link"),
                    search=game_name
                )
            )

    return games
