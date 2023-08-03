from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import CallbackQuery
from loader import bot


# from config import API


def product_btn(category, page, NEXT_API):
    markup = InlineKeyboardMarkup()
    max_page = 58
    # ---------- data
    import requests

    payload = ""
    headers = {}
    response = requests.request("POST", NEXT_API + f'&page={page}', headers=headers, data=payload).json()
    products_data = response['result']['products']['data']

    for product in products_data:
        markup.add(
            InlineKeyboardButton(product['name'][:10] + " " + product['title'][:20],
                                 callback_data=f"product|{product['id']}"))

    preview_btn = InlineKeyboardButton('◀️', callback_data='preview_btn')
    page_btn = InlineKeyboardButton(page, callback_data=f'page|{category}')
    next_btn = InlineKeyboardButton('▶️', callback_data='next_btn')

    main_menu = InlineKeyboardButton('Главное меню ↩️', callback_data='mein_menu')
    category_back = InlineKeyboardButton('⏮ назад', callback_data='category_back')

    if page == 1:
        markup.row(page_btn, next_btn)
    elif 1 < page < max_page:
        markup.row(preview_btn, page_btn, next_btn)
    elif page == max_page:
        markup.row(preview_btn, page_btn)

    markup.row(category_back, main_menu)
    return markup


def product_item():
    markup = InlineKeyboardMarkup()
    back = InlineKeyboardButton('❌ Удалить', callback_data=f'delete')
    category_menu = InlineKeyboardButton('Каталог: 🛍', callback_data=f'category_back')
    markup.add(back)
    markup.add(category_menu)
    return markup
