from telebot import TeleBot
from flask_injector import Binder

from bot import TelegramWebhookHelper


# Bootstrap
def bootstrap_factory(bot: TeleBot) -> callable:
    def configure(binder: Binder):
        # Initiation
        tw = TelegramWebhookHelper(bot)

        # Binding - Helper
        binder.bind(TelegramWebhookHelper, to=tw)
    
    return configure
