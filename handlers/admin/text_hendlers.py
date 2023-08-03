from telebot.types import Message, ReplyKeyboardRemove

from keyboards.default import admin_btn
from loader import bot, db
from config import ADMIN
from states import CopyAdminState


@bot.message_handler(func=lambda message: message.text == "Foydalanuvchilar soni", chat_id=ADMIN)
def reaction_count_user(message: Message):
    chat_id = message.chat.id
    user = db.count_user()
    bot.send_message(chat_id, f'Hozirda Quraiz telegram botida {user} ta foydalnuvchi mavjud !!!')


@bot.message_handler(func=lambda message: message.text == "Habar jo'natish", chat_id=ADMIN)
def reaction_sent_message(message: Message):
    chat_id = message.chat.id
    bot.set_state(message.from_user.id, CopyAdminState.copy, chat_id)
    bot.send_message(chat_id, 'habar yozishingiz mumkin', reply_markup=ReplyKeyboardRemove())


@bot.message_handler(
    content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location",
                   "contact"], state=CopyAdminState.copy)
def reaction_copy(message: Message):
    chat_id = message.chat.id
    users_id = message.from_user.id
    users = [item[0] for item in db.users_ids()]
    count_user = db.count_user()
    count = 0
    for user in users:
        try:
            bot.copy_message(user, chat_id, message.message_id)
            count += 1
        except:
            # bot.send_message(chat_id, f"{user} ga jo'natilmadi")
            pass
    bot.delete_state(users_id, chat_id)
    bot.send_message(chat_id, f'{count}/{count_user} ta obunachiga jonatildi !', reply_markup=admin_btn())
