import logging
import sys

from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Ciao Flutter Dev!')


def main():
    """ Run bot """

    # Read token from parameters
    token = sys.argv[1]

    updater = Updater(token)
    dp = updater.dispatcher

    # List of commands available
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
