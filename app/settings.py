import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")

# API KEY
CUSTOM_SEARCH_API = os.environ.get("CUSTOM_SEARCH_API")

SEARCH_URL = 'https://www.googleapis.com/customsearch/v1?cx={}&key={}&q='.format(
    SEARCH_ENGINE_ID, CUSTOM_SEARCH_API
)

WEBS = ("eneba", "instantgaming", "amazon")

# More info: https://api.rawg.io/docs/
GAMES_API = "https://api.rawg.io/api/games/"

PLATFORMS = (
    "pc",
    "xbox360"
    "xbox 360",
    "xbox one",
    "playstation 3",
    "ps3",
    "playstation 4",
    "ps4",
)
