import random

from scrapper.settings import USER_AGENTS, DELAYS


def get_random_ua():
    return random.choice(USER_AGENTS)


def get_random_delay():
    return random.choice(DELAYS)


def formatting_price(price: str):
    return price.replace("\xa0", " ").replace("\x80", "€")


def formatting_price_2(price: str):
    return price.replace("\x82", "€")
