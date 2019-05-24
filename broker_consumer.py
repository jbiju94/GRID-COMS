import sys
import os
import atexit
import json

from confluent_kafka import KafkaException, KafkaError
from app.message_broker.utils import get_message_broker_topic, get_message_broker_consumer

from app.telegram.telegram_bot import TelegramBot

if __name__ == '__main__':

    topics = get_message_broker_topic()
    c = get_message_broker_consumer()
    c.subscribe(topics)
    atexit.register(c.close())
    while True:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            # Error or event
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                # Error
                raise KafkaException(msg.error())
        else:
            # Proper message
            message = json.loads(msg.value())
            bot = TelegramBot(bot_token=os.environ['TELEGRAM_API'])
            bot.send_message(message['chat_id'], message['message'])
            sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' % (msg.topic(), msg.partition(), msg.offset(),
                                                                         str(msg.key())))
            print(msg.value())
