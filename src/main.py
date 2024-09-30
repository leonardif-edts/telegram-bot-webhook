import json

from flask import Flask, request, current_app, jsonify
from flask_injector import FlaskInjector
from telebot import TeleBot

from config import Config
from bot import TelegramWebhookHelper
from bootstrap import bootstrap_factory


# Init Service
C = Config()

app = Flask(__name__)
bot = TeleBot(C.BOT_TOKEN.get_secret_value(), threaded=False)

# Configure WebHook Handler
from handler import configure_webhook
configure_webhook(bot)


# WebHook Endpoint
@app.post("/webhook")
def webhook(tw: TelegramWebhookHelper):
    req_body = request.get_json()
    try:
        tw.update_bot(req_body)
        current_app.logger.info(req_body)
    except Exception:
        current_app.logger.error(json.dumps(req_body))
    return jsonify({"msg": "Success"})

# Inject Dependencies
FlaskInjector(app=app, modules=[bootstrap_factory(bot)])
