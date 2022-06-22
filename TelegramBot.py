from asyncore import dispatcher
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.dispatcher import Dispatcher
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Bot

updater = Updater("5517859423:AAHLtuyyojK8yT4xszKAJTdl8UorAGSbZFg", use_context=True)

dispatcher: Dispatcher = updater.dispatcher

def start(update: Update, context:CallbackContext):
    #Callback for handling start command
    bot: Bot = context.bot

    bot.send_message(chat_id=update.effective_chat.id, text="Hello User, You have used the start command. Type /help to see the list of commands")


dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
