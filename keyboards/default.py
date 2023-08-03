from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from image import *


def main_menu_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton('Каталог Товаров: 🛒'), KeyboardButton('Контакты: 📞'))
    markup.row(KeyboardButton('Помощь: ⚙️'))
    return markup


# def register_btn():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton("Ro'yhatdan o'tish 📝"))
#     return markup


def product_catalog():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.row(KeyboardButton('Новинки 🆕'))
    markup.row(KeyboardButton("Стройматериалы 👷"), KeyboardButton("Инструмент 🛠"))
    markup.row(KeyboardButton("Электрика ⚡️"), KeyboardButton("Инженерные системы 🏗"))
    markup.row(KeyboardButton("Интерьер и отделка 🖼"), KeyboardButton("Сантехника 🚰"))
    markup.row(KeyboardButton("Крепеж 🔩"), KeyboardButton("Благоустройство 🧹"))
    markup.add(KeyboardButton('Orqaga ↩️'))
    return markup


def back():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Orqaga ↩️'))
    return markup


# ------------------ Admin --------------------------


def admin_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('Foydalanuvchilar soni'),
        KeyboardButton('Habar jo\'natish'),

    )
    return markup