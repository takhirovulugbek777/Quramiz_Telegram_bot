from telebot.types import CallbackQuery

from config import API, DETAIL_API
from loader import bot
from keyboards.default import *
from keyboards.inline import *


# @bot.callback_query_handler(func=lambda call: call)
# def reaction_callbacks(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     bot.send_message(chat_id, 'ishladi')


@bot.callback_query_handler(func=lambda call: call.data == 'next_btn')
def reaction_to_next(call: CallbackQuery):
    chat_id = call.message.chat.id
    item = call.message.reply_markup.keyboard[-2]
    for key in item:
        if 'page' in key.callback_data:
            category = key.callback_data.split('|')[1]
            if category == "Стройматериалы 👷":
                num_category = '1/'
            elif category == 'Инструмент 🛠':
                num_category = '2/'
            elif category == "Электрика ⚡️":
                num_category = '3/'
            elif category == "Инженерные системы 🏗":
                num_category = '4/'
            elif category == "Интерьер и отделка 🖼":
                num_category = '5/'
            elif category == "Сантехника 🚰":
                num_category = '6/'
            elif category == "Крепеж 🔩":
                num_category = '7/'
            elif category == "Благоустройство 🧹":
                num_category = '8/'
            elif category == 'Новинки 🆕':
                num_category = '9/'
            else:
                num_category = '1/'
            page = int(key.text)
            page += 1
            API_NEXT = API + num_category
            bot.edit_message_reply_markup(chat_id, call.message.id, reply_markup=product_btn(category, page, API_NEXT))


@bot.callback_query_handler(func=lambda call: call.data == 'preview_btn')
def reaction_to_preview(call: CallbackQuery):
    chat_id = call.message.chat.id
    keyboard = call.message.reply_markup.keyboard[-2]
    for key in keyboard:
        if 'page' in key.callback_data:
            category = key.callback_data.split('|')[1]

            if category == "Стройматериалы 👷":
                num_category = '1/'
            elif category == 'Инструмент 🛠':
                num_category = '2/'
            elif category == "Электрика ⚡️":
                num_category = '3/'
            elif category == "Инженерные системы 🏗":
                num_category = '4/'
            elif category == "Интерьер и отделка 🖼":
                num_category = '5/'
            elif category == "Сантехника 🚰":
                num_category = '6/'
            elif category == "Крепеж 🔩":
                num_category = '7/'
            elif category == "Благоустройство 🧹":
                num_category = '8/'
            elif category == 'Новинки 🆕':
                num_category = '9/'
            else:
                num_category = '1/'
            page = int(key.text)
            page -= 1
            API_NEXT = API + num_category
            bot.edit_message_reply_markup(chat_id, call.message.id, reply_markup=product_btn(category, page, API_NEXT))


@bot.callback_query_handler(func=lambda call: call.data == 'mein_menu')
def reaction_main_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, 'Главное меню:', reply_markup=main_menu_btn())


@bot.callback_query_handler(func=lambda call: call.data == 'category_back')
def reaction_main_menu(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
    bot.send_message(chat_id, 'Каталог Товаров', reply_markup=product_catalog())


# @bot.callback_query_handler(func=lambda call: 'page' in call.data)
# def reaction_page(call: CallbackQuery):
#     keyboard = call.message.reply_markup.keyboard[-2]
#     for key in keyboard:
#         if 'page' in key.callback_data:
#             page = key.text
#             bot.answer_callback_query(call.id, f"Siz {page} page dasiz")

@bot.callback_query_handler(func=lambda call: 'product' in call.data)
def reaction_product(call: CallbackQuery):
    import requests
    page = 1
    item = call.message.reply_markup.keyboard[-2]
    chat_id = call.message.chat.id
    for key in item:
        page = key.text
    product_id = str(call.data.split('|')[1])
    # detail_id = product_id.split(' ')[1]
    response = requests.request("GET", DETAIL_API + f'{product_id}').json()
    detail_data = response['result']
    detail_name = detail_data['name']
    detail_title = detail_data['title']
    # ---------- description --------------
    detail_info = detail_data['info']
    # category_id = detail_data['category_id']
    detail_price = detail_data['price']
    detail_photo = detail_data['photo']
    photo = f'https://e-pos.uz/uploads/products/medium/{detail_photo}'
    detail_count = detail_data['count']
    # print(detail_id, detail_name, detail_title, detail_kv_m, detail_count, detail_photo)

    bot.send_photo(chat_id, photo, caption=f'''
    <strong>🚧 {detail_name}</strong>
<strong>✅ Размер: {detail_title}</strong>
<strong>✅ Цена: {detail_price}</strong> сум 🔥
<strong>✅ В наличии: {detail_count} шт</strong>

<a href="https://quramiz.uz/cl/product/{product_id}"><strong>Покупка товаров : Покупка</strong></a>

📞 Phone: +998 (71) 205 81 80

<a href="https://t.me/sqbc_uz"><strong>📱Telegram</strong></a> | <a href="https://quramiz.uz/"><strong>🌐Websites</strong></a> | <a href="https://www.instagram.com/quramiz.uz/"><strong>📸Instagram</strong></a>
''',
                   parse_mode='HTML',
                   reply_markup=product_item())


@bot.callback_query_handler(func=lambda call: 'delete' in call.data)
def reaction_delete(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.id)
