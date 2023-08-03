from telebot.types import Message, ReplyKeyboardRemove
from config import API

from config import *
from keyboards.inline import *
from loader import bot
from keyboards.default import *


# reaction for 'buy btn'

@bot.message_handler(func=lambda message: message.text == 'Каталог Товаров: 🛒')
def reaction_catalog(message: Message):
    chat_id = message.chat.id
    # check = db.check_user(user_id)
    # if None in check:
    #     # bot.send_message(chat_id, 'royhatdan otish kerak', reply_markup=register_btn())
    #     pass
    bot.send_message(chat_id, 'Выберите каталог 😎', reply_markup=product_catalog())


# call -> aloqa tugmasi

@bot.message_handler(func=lambda message: message.text == 'Контакты: 📞')
def reaction_call(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     '''Телефоны:  
                     +998(71)2058180 
                     +998(71)2445105
                     
Email:
                office@quramiz.uz
                            
Все каналы связи: 

    Telegram:   
                https://t.me/sqbc_uz
                                                                 
    Instagram:  
                https://www.instagram.com/sqb.construction/ 
                                                                 
    Facebook:   
               https://www.facebook.com/sqbc.uz/
                                                                 
Время работы пунктов выдачи заказов:  
                                                      
        Ежедневно с 08:00 до 20:00        
         ''', reply_markup=back())


# help button

@bot.message_handler(func=lambda message: message.text == 'Помощь: ⚙️')
def reaction_call(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '''
        Помощь:
        
    💴 Оплата:
    🚛 Доставка:
    🛠 Гарантия:
    🔙 Возврат товара:
    💲 Кредит:
    ❓ FAQ:
        
    Больше информации:
    
        ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
        
        https://quramiz.uz/cl/help
        

    ''', reply_markup=back())


# back reaction

@bot.message_handler(content_types=['text'], func=lambda message: message.text == 'Orqaga ↩️')
def reaction_main_menu(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Asosiy menu', reply_markup=main_menu_btn())


# # ------------------------ image for catalog -------------
# photo1 = open(r"D:\Quramiz Bot\quramiz\image\1.jpg", 'rb')
# photo2 = open(r"D:\Quramiz Bot\quramiz\image\2.jpg", 'rb')
# photo3 = open(r"D:\Quramiz Bot\quramiz\image\3.jpg", 'rb')
# photo4 = open(r"D:\Quramiz Bot\quramiz\image\4.jpg", 'rb')
# photo5 = open(r"D:\Quramiz Bot\quramiz\image\5.jpg", 'rb')
# photo6 = open(r"D:\Quramiz Bot\quramiz\image\6.jpg", 'rb')
# photo7 = open(r"D:\Quramiz Bot\quramiz\image\7.jpg", 'rb')
# photo8 = open(r"D:\Quramiz Bot\quramiz\image\8.jpg", 'rb')
# # ------------------------ end catalog -------------------

# ------------------------- stroy material --------------------- #

@bot.message_handler(func=lambda message: message.text == 'Стройматериалы 👷')
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = 'Стройматериалы 👷'
    page = 1
    NEXT_API = API + "1/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


# ------------------------------ belongings -------------------


# @bot.message_handler(func=lambda message: message.text == 'Инструмент 🛠')
# def reaction_ca(message: Message):
#     chat_id = message.chat.id
#     category = message.text
#     import requests
#
#     payload = ""
#     headers = {}
#     response = requests.request("POST", API_NEXT, headers=headers, data=payload).json()
#     products_data = response['result']['products']['data']
#     # for item in products_data:
#     #     result = {"https://quramiz.uz/cl/product/" + str(item['id']), item['name'], item['price'], "so'm",
#     #               'https://e-pos.uz/uploads/products/medium/' + item['photo']}
#     bot.send_message(chat_id, 'maxsulotlar', reply_markup=product_btn(products_data, category))

# ---------------------- end test


# ---------------------------- main instrumentation's


@bot.message_handler(func=lambda message: message.text == 'Инструмент 🛠')
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = 'Инструмент 🛠'
    page = 1
    NEXT_API = API + "2/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


@bot.message_handler(func=lambda message: message.text == "Электрика ⚡️")
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = "Электрика ⚡️"
    page = 1
    NEXT_API = API + "3/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


@bot.message_handler(func=lambda message: message.text == "Инженерные системы 🏗")
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = "Инженерные системы 🏗"
    page = 1
    NEXT_API = API + "4/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


@bot.message_handler(func=lambda message: message.text == "Интерьер и отделка 🖼")
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = "Интерьер и отделка 🖼"
    page = 1
    NEXT_API = API + "5/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


@bot.message_handler(func=lambda message: message.text == "Сантехника 🚰")
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = "Сантехника 🚰"
    page = 1
    NEXT_API = API + "6/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


@bot.message_handler(func=lambda message: message.text == "Крепеж 🔩")
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = "Крепеж 🔩"
    page = 1
    NEXT_API = API + "7/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


@bot.message_handler(func=lambda message: message.text == "Благоустройство 🧹")
def reaction_ca(message: Message):
    chat_id = message.chat.id
    category = "Благоустройство 🧹"
    page = 1
    NEXT_API = API + "8/"
    bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(chat_id, message.id + 1)
    bot.send_message(chat_id, 'Продукты 🛠', reply_markup=product_btn(category, page, NEXT_API))


# @bot.message_handler(func=lambda message: message.text == 'Новинки 🆕')
# def reaction_ca(message: Message):
#     chat_id = message.chat.id
#     category = 'Новинки 🆕'
#     page = 1
#     NEXT_API = API + "9/"
#     bot.send_message(chat_id, '.', reply_markup=ReplyKeyboardRemove())
#     bot.delete_message(chat_id, message.id + 1)
#     bot.send_message(chat_id, 'maxsulotlar', reply_markup=product_btn(category, page, NEXT_API))

@bot.message_handler(func=lambda message: message.text)
def reaction_ca(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '''
Вы можете позвонить в офис для получения дополнительной информации

📱 Telegram : @quramiz_support
📨 Email : office@quramiz.uz    
📞 Phone: +998(71) 205 81 80
    ''', reply_markup=product_catalog())
