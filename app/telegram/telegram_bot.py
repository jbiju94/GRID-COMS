from flask import request
import requests


class TelegramBot:

    URL_TEMPLATE = 'https://api.telegram.org/bot<token>/'

    def __init__(self, bot_token, url=None):
        self.token = bot_token
        self.base_url = TelegramBot.URL_TEMPLATE.replace('<token>', self.token)

    def test_bot(self) -> dict:
        endpoint = 'getMe'

        r = requests.get(url=self.base_url+endpoint)
        if r.status_code != 200:
            raise Exception(r.content)
        else:
            return dict(r.json())

    """
    Webhook Handling for updates
    """
    def set_webhook(self, webhook_url):
        endpoint = 'setWebhook'
        params = {'url': webhook_url}

        r = requests.get(url=self.base_url+endpoint, params=params)
        if r.status_code != 200:
            raise Exception(r.content)

    def get_webhook(self) -> dict:
        endpoint = 'getWebhookInfo'

        r = requests.get(url=self.base_url + endpoint)
        if r.status_code != 200:
            raise Exception(r.content)
        else:
            return dict(r.json())

    def delete_webhook(self):
        endpoint = 'deleteWebhook'

        r = requests.get(url=self.base_url + endpoint)
        if r.status_code != 200:
            raise Exception(r.content)

    """
    Messaging Operations
    """
    def send_message(self, chat_id, message, reply_to_message_id=None):
        endpoint = 'sendMessage'
        params = {'chat_id': chat_id, 'text': message}
        if reply_to_message_id is not None :
            params.update({'reply_to_message_id':reply_to_message_id})

        r = requests.get(url=self.base_url + endpoint, params=params)

        if r.status_code != 200:
            raise Exception(r.content)

    def get_chat(self, chat_id) -> dict:
        endpoint = 'getChat'
        params = {'chat_id': chat_id}

        r = requests.get(url=self.base_url + endpoint, params=params)

        if r.status_code != 200:
            raise Exception(r.content)
        else:
            return dict(r.json())

    def pin_message(self, chat_id, message_id):
        endpoint = 'pinChatMessage'
        params = {'chat_id': chat_id, 'message_id': message_id, 'disable_notification': True}

        r = requests.get(url=self.base_url + endpoint, params=params)

        if r.status_code != 200:
            raise Exception(r.content)

    def unpin_message(self, chat_id):
        endpoint = 'unpinChatMessage'
        params = {'chat_id': chat_id}

        r = requests.get(url=self.base_url + endpoint, params=params)

        if r.status_code != 200:
            raise Exception(r.content)
