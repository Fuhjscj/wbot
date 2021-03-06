import random

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# --
from commander.commander import Commander
from vk_bot import VkBot
# --


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "3dc507ab92ffa01ff8bcad1f0cbd915c87f1eedb30ddfe58202e17cad410a092c812ddf5a5a538abdca4f"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkBotLongPoll(vk,"204077562")

commander = Commander()
print("Server started")
for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:

        if event.from_chat:

            print(f'New message from {event.user_id}', end='')

            bot = VkBot(event.user_id)

            if event.text[0] == "/":
                write_msg(event.user_id, commander.do(event.text[1::]))
            else:
                write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
            print("-------------------")
