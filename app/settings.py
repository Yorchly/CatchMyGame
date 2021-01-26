import os

from app.models.games_cached import GamesCached

BOT_TOKEN = os.environ.get("BOT_TOKEN")

SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID")

# API KEY
CUSTOM_SEARCH_API = os.environ.get("CUSTOM_SEARCH_API")

SEARCH_URL = 'https://www.googleapis.com/customsearch/v1?cx={}&key={}&q='.format(
    SEARCH_ENGINE_ID, CUSTOM_SEARCH_API
)

WEBS = ("eneba", "instantgaming", "steam store")

GAMES_CACHED = GamesCached()
