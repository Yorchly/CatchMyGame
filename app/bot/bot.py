import logging
from telegram.ext import Updater, CommandHandler

from app.bot.bot_commands import BotCommands
from app.settings import BOT_TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self):
        self.__updater = Updater(token=BOT_TOKEN, use_context=True)
        self.__add_handlers()
        try:
            self.__updater.start_polling()
            logger.info("Bot started...")
            self.__updater.idle()
        except Exception as e:
            logger.error(f"Error starting bot -> {e}")
            raise e

    def __add_handlers(self):
        """
        Add handlers to dispatcher in order to commands to work properly. New commands must to be added to
        commands dict.
        :return:
        """
        dispatcher = self.__updater.dispatcher

        # Getting commands from BotCommands. Function name will be the name of the command.
        for func_name in dir(BotCommands):
            func = getattr(BotCommands, func_name)
            if callable(func) and not func_name.startswith("__"):
                dispatcher.add_handler(CommandHandler(func_name, func))
