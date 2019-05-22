import sys
import os

from confluent_kafka import Producer


def get_message_broker_producer():
    conf = {
        'bootstrap.servers': os.environ['CLOUDKARAFKA_BROKERS'],
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'SCRAM-SHA-256',
        'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
        'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD']
    }
    return Producer(**conf)


def get_message_broker_topic():
    return os.environ['CLOUDKARAFKA_TOPIC_PREFIX'] + "notification"
