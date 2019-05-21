from flask import Blueprint, render_template, abort, Response, jsonify
import os
from app.telegram.telegram_bot import TelegramBot

telegram = Blueprint('telegram', __name__, template_folder='templates', url_prefix='/telegram/v1')


@telegram.route('/bot', methods=['GET'])
def def_resp():
    bot = TelegramBot(bot_token=os.environ['TELEGRAM_API'])
    return jsonify(bot.test_bot())


@telegram.route('/setWebhook', methods=['GET'])
def set_webhook(webhook_url):
    bot = TelegramBot(bot_token=os.environ['TELEGRAM_API'])
    try:
        bot.set_webhook(webhook_url)
        return Response("OK", status=200)
    except Exception as e:
        return Response(str(e), status=200)


@telegram.route('/notify/message', methods=['POST'])
def notify_new_message():

    return Response("OK", status=200)
