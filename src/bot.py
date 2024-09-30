import json

from telebot import TeleBot
from telebot.types import Update


# Helper
class TelegramWebhookHelper:
    __bot: TeleBot

    def __init__(self, bot: TeleBot):
        self.__bot = bot

    def update_bot(self, data: dict) -> str:
        update = Update.de_json(json.dumps(data))
        self.__bot.process_new_updates([update])
