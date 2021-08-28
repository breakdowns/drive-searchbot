from telegram.ext import CommandHandler, run_async
from bot import dispatcher, updater, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list


@run_async
def start(update, context):
    start_string = f'''
This bot can search file from your Google Drive!
'''
    sendMessage(start_string, context.bot, update)


@run_async
def log(update, context):
    sendLogFile(context.bot, update)


botcmds = [
        (f'{BotCommands.ListCommand}','Searches files in Drive')
    ]


def main():
    bot.set_my_commands(botcmds)

    start_handler = CommandHandler(BotCommands.StartCommand, start, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(log_handler)

    updater.start_polling()
    LOGGER.info("Bot Started!")
    updater.idle()

main()
