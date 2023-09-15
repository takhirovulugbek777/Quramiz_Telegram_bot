from telebot.types import Message

from loader import bot, db
# add for save user id in database -> from loader import db
from keyboards.default import *


@bot.message_handler(commands=['help', 'start'], chat_types=['private'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    db.save_user(user_id)  # Save telegram_id
    db.save_user_name(user_id, user_name)  # Save full_name

    bot.send_message(chat_id,
                     f'Здравствуйте {message.from_user.full_name}, добро пожаловать в Quramiz (официальный) бот!!!',
                     reply_markup=main_menu_btn())
