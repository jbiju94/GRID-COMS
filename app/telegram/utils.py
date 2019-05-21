def parse_message(message) -> dict:
    return {
        'chat_id': message['message']['chat']['id'],
        'user': message['message']['chat']['username'],
        'message': message['message']['text']
    }
