import os

from app.models.games_cached import GamesCached

BOT_TOKEN = os.environ.get("BOT_TOKEN")

GAMES_CACHED = GamesCached()

ENEBA_FILENAME = "eneba.jl"

INSTANTGAMING_FILENAME = "instantgaming.jl"

STEAM_FILENAME = "steam.jl"
