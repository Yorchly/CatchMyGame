import logging

import telegram
from telegram.ext import Updater, CommandHandler

from app.decorators import clean_cache
from app.settings import BOT_TOKEN, WEBS, PLATFORMS
from app.utils import search_in_api, search_in_game_api

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class TelegramBot:
    __help_text = "Los comandos que posee el bot son los siguientes (sin las comillas '' especificadas):\n\n " \
                  "- '/search [nombre_juego]' -> Busca el juego en las páginas precargadas en el " \
                  "bot. Ej: '/search Nier Automata'.\n\n " \
                  "- '/help' -> Muestra los comandos disponibles para el bot.\n\n "

    def __init__(self):
        self.__updater = Updater(token=BOT_TOKEN, use_context=True)
        self.__add_handlers()

    """
    ############# PRIVATE METHODS ############# 
    """

    def __start(self, update, context):
        """
        Function to treat /start command. It'll show a welcome message with the list of commands.
        :param update:
        :param context:
        :return:
        """
        start_message = "Bienvenido al bot CatchMyGame, {}. \n\nEn este bot puede encontrar el juego deseado en " \
                        "las páginas precargadas y ver en dónde está más barato " \
                        "\U0001F60D\U0001F4B8.\n\n".format(update.effective_user.name) + self.__help_text + \
                        "Espero que lo disfrute. \U0001F31A \n\n" \
                        "<i>Bot realizado por Yorchly cuyo código está disponible en: {}\n" \
                        "Las comprobaciones de los juegos se realizan gracias a la API proporcionada por " \
                        "RAWG ({})</i>".format(
                            "https://github.com/Yorchly/CatchMyGame",
                            "https://rawg.io/"
                        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=start_message,
            parse_mode=telegram.ParseMode.HTML
        )

    def __help(self, update, context):
        """
        Function to treat /help command. It'll show a list with Bot's commands.
        :param update:
        :param context:
        :return:
        """
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self.__help_text
        )

    @staticmethod
    @clean_cache
    def __search(update, context):
        game_name = " ".join(list(map(lambda x: x.lower() if x.lower() not in PLATFORMS else "", context.args)))

        game_name_for_search = search_in_game_api(game_name)

        if game_name_for_search:
            for web in WEBS:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=search_in_api(game_name_for_search, web)
                )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="No se ha encontrado el juego especificado \U0001F62D"
            )

    def __add_handlers(self):
        """
        Add handlers to dispatcher in order to commands to work properly. New commands must to be added to
        commands dict.
        :return:
        """
        dispatcher = self.__updater.dispatcher
        # IMPORTANT: you must add new commands to this dict in order to apply the handlers.
        commands = {
            "start": self.__start,
            "help": self.__help,
            "search": self.__search
        }

        for command_name, command_function in commands.items():
            dispatcher.add_handler(CommandHandler(command_name, command_function))

    """
    ############# PUBLIC METHODS ############# 
    """

    def start_bot(self):
        self.__updater.start_polling()
        self.__updater.idle()
