import re
import time

import telegram

from app.bot.utils import get_games_results
from app.constants.messages import HELP_TEXT, START_MESSAGE, PROCESSING_REQUEST, GAME_NOT_FOUND, GAME_MESSAGE
from app.settings import GAMES_CACHED


class BotCommands:
    @staticmethod
    def start(update, context):
        """
        Function to treat /start command. It'll show a welcome message with the list of commands.
        :param update:
        :param context:
        :return:
        """
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=START_MESSAGE.format(update.effective_user.name),
            parse_mode=telegram.ParseMode.HTML
        )

    @staticmethod
    def help(update, context):
        """
        Function to treat /help command. It'll show a list with Bot's commands.
        :param update:
        :param context:
        :return:
        """
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=HELP_TEXT
        )

    @staticmethod
    def search(update, context):
        game_name = " ".join(
            re.findall(
                r'[a-zA-Z0-9]+', ' '.join(context.args)
            )
        ).lower()

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=PROCESSING_REQUEST
        )

        games = GAMES_CACHED.search_game_by_name_in_search(game_name)

        if not games:
            games = get_games_results(game_name)
            GAMES_CACHED.add_games(games)

        for game in games:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                parse_mode=telegram.ParseMode.HTML,
                text=GAME_MESSAGE.format(game.title, game.price, game.link)
            )

        if not games:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=GAME_NOT_FOUND
            )

        GAMES_CACHED.check_time_and_clean()
