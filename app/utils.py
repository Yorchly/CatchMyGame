from decimal import Decimal
from datetime import datetime, timedelta

import requests

from app.settings import SEARCH_URL, GAMES_API, CACHED_DATA, TIME_CACHED_DATA


def get_cached_data(game_name):
    """
    Get game data that is cached in CACHED_DATA dict.
    :param game_name:
    :type game_name: str
    :return: dict with game info if game is cached, False if not.
    """
    if game_name in CACHED_DATA:
        return CACHED_DATA.get(game_name)
    else:
        return False


def set_game_in_cached_data(game_name, link, price, currency):
    """
    Set game data in dict of cached data.
    :param game_name:
    :type game_name: str
    :param link:
    :type link: str
    :param price:
    :type price: Decimal
    :param currency:
    :type currency: str
    :return:
    """
    data = {
        "link": link,
        "price": price,
        "currency": currency,
        "last_update": datetime.now()
    }
    if game_name in CACHED_DATA:
        CACHED_DATA.get(game_name).update(data)
    else:
        CACHED_DATA[game_name] = data


def check_last_update_cached_data(game_name):
    """
    Check if last time that game data was updated is not greater than TIME_CACHED_DATA minutes.
    :param game_name:
    :type game_name: str
    :return: True in case that last time data was updated is greater than TIME_CACHED_DATA minutes, False if it's not.
    """
    diff = datetime.now() - CACHED_DATA.get(game_name).get("last_update")

    if (diff.seconds / 60) >= TIME_CACHED_DATA:
        return True
    else:
        return False


def search_in_api(game_name, web):
    """

    :param game_name:
    :param web:
    :return:
    """
    response = requests.get(SEARCH_URL+"{}+{}".format(game_name, web))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error buscando en la API"

    parsed_response = response.json()
    name = parsed_response.get("items")[0].get("title")
    link = parsed_response.get("items")[0].get("link")
    if web != "amazon":
        price = Decimal(parsed_response.get("items")[0].get("pagemap").get("offer")[0].get("price"))
        currency = parsed_response.get("items")[0].get("pagemap").get("offer")[0].get("pricecurrency")
    else:
        price = Decimal(0)
        currency = "No se ha podido obtener"

    return "Nombre: {}\n" \
           "Precio: {}\n" \
           "Moneda: {}\n" \
           "Enlace: {}".format(name, price if price > Decimal(0) else "No se ha podido obtener", currency, link)


def search_in_game_api(game_name):
    """
    Check in GAMES_API if game searched by user exists. If response return a redirect, the game exists but with
    a different slug in API.
    :param game_name:
    :return:
    """
    response = requests.get(GAMES_API+game_name).json()

    if response.get("redirect"):
        return True
    elif response.get("detail") == "Not found.":
        return False
    else:
        return True
