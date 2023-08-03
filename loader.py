import telebot
from telebot.storage import StateMemoryStorage
from telebot import custom_filters
from telebot.types import BotCommand

from config import API_TOKEN

# import database
from database import DataBase

# detail data base
db = DataBase()

bot = telebot.TeleBot(API_TOKEN, state_storage=StateMemoryStorage(), use_class_middlewares=True)

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.ChatFilter())

bot.set_my_commands(
    commands=[
        BotCommand('start', 'Start the bot ....'),
        BotCommand('help', 'Help center')
    ]
)
cmd = bot.get_my_commands(scope=None, language_code=None)
