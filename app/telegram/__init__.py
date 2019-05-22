from flask import Blueprint, request, Response, jsonify
import os
from app.telegram.telegram_bot import TelegramBot
from app.telegram.utils import parse_message
from app.message_broker import get_message_broker_producer, get_message_broker_topic

telegram = Blueprint('telegram', __name__, template_folder='templates', url_prefix='/telegram/v1')


@telegram.route('/bot', methods=['GET'])
def def_resp():
    bot = TelegramBot(bot_token=os.environ['TELEGRAM_API'])
    return jsonify(bot.test_bot())


@telegram.route('/setWebhook', methods=['GET'])
def set_webhook():
    bot = TelegramBot(bot_token=os.environ['TELEGRAM_API'])
    url = request.args.get('url')
    try:
        bot.set_webhook(url)
        return Response("OK", status=200)
    except Exception as e:
        return Response(str(e), status=200)


@telegram.route('/notify/message', methods=['POST'])
def notify_new_message():
    message = parse_message(request.get_json())
    bot = TelegramBot(bot_token=os.environ['TELEGRAM_API'])
    bot.send_message(message['chat_id'], message['message'])

    # Push is to Queue
    producer = get_message_broker_producer()
    producer.produce(get_message_broker_topic(), message)
    producer.flush()

    return Response("OK", status=200)
