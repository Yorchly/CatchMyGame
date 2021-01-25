import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")

# API KEY
CUSTOM_SEARCH_API = os.environ.get("CUSTOM_SEARCH_API")

SEARCH_URL = 'https://www.googleapis.com/customsearch/v1?cx={}&key={}&q='.format(
    SEARCH_ENGINE_ID, CUSTOM_SEARCH_API
)

WEBS = ("eneba", "instantgaming")

# More info: https://api.rawg.io/docs/
GAMES_API = "https://api.rawg.io/api/games?search="

# Data in cached var will be update after 2 minutes.
TIME_CACHED_DATA = float(2)

# All cached var will be clear every 5 min
TIME_TO_CLEAN_CACHED_VAR = float(5)

# Used to get a query faster. Data stored in CACHED_DATA will be updated depending on the minutes specified in
# TIME_CACHED_DATA.
CACHED_DATA = {}
