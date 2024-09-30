from telebot import TeleBot
from telebot.types import Message

from main import bot

# Configure
def configure_webhook(bot: TeleBot):
    bot.message_handler(regexp="^!report")(generate_report)


# Handler
def generate_report(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Report ABC (from Message Handler)")
