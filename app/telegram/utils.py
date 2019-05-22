def parse_message(message) -> dict:
    return {
        'chat_id': message['message']['chat']['id'],
        'root_message_id': message['message']['message_id'],
        'user': message['message']['chat']['username'],
        'message': message['message']['text']
    }
