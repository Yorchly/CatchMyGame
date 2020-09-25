import logging

from telegram.ext import Updater, CommandHandler

from app.settings import BOT_TOKEN


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class TelegramBot:
    __help_text = "Los comandos que posee el bot son los siguientes (sin las comillas '' especificadas):\n\n " \
                  "- '/search [nombre_juego]' -> Busca el juego en una de las páginas precargadas en la " \
                  "aplicación\n\n " \
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
        start_message = "Bienvenido al bot CatchMyGame, {}. \n\nEn este bot puede encontrar el juego deseado en una " \
                        "de las páginas precargadas y ver en dónde está más barato " \
                        "\U0001F60D\U0001F4B8.\n\n".format(update.effective_user.name) + self.__help_text + \
                        "Espero que lo disfrute. \U0001F31A"
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=start_message
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
    def __search(update, context):
        # TODO -> Add search method.
        pass

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
