from telebot.types import Message

from loader import bot, db
from config import ADMIN
from keyboards.default import admin_btn


@bot.message_handler(commands=['help', 'start'], chat_id=ADMIN)
def reaction_admin_commands(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'salom {message.from_user.full_name}', reply_markup=admin_btn())
