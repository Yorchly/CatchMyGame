import os

from app.models.games_cached import GamesCached

BOT_TOKEN = os.environ.get("BOT_TOKEN")

GAMES_CACHED = GamesCached()

ENV = os.environ.get("ENV", "debug")

PORT = int(os.environ.get('PORT', '8443'))

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
