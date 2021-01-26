import re

import telegram

from app.bot.search import search_game
from app.constants.messages import HELP_TEXT, START_MESSAGE, PROCESSING_REQUEST, GAME_NOT_FOUND, GAME_MESSAGE
from app.settings import WEBS, GAMES_CACHED


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
        one_game_found = False
        game_name = " ".join(
            re.findall(
                r'[a-zA-Z0-9]+', ' '.join(context.args)
            )
        ).lower()

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=PROCESSING_REQUEST
        )

        games_in_cache = GAMES_CACHED.search_game_by_name(game_name)

        if game_name:
            if not games_in_cache:
                for web in WEBS:
                    game = search_game(game_name, web)
                    if game:
                        one_game_found = True
                        GAMES_CACHED.add_game(game)
                        context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            parse_mode=telegram.ParseMode.HTML,
                            text=GAME_MESSAGE.format(game.name, game.price, game.currency, game.link)
                        )

                if not one_game_found:
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=GAME_NOT_FOUND
                    )
            else:
                for game in games_in_cache:
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        parse_mode=telegram.ParseMode.HTML,
                        text=GAME_MESSAGE.format(game.name, game.price, game.currency, game.link)
                    )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=GAME_NOT_FOUND
            )

        GAMES_CACHED.check_time_and_clean()
