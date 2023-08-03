from loader import bot, db

import handlers
from middleware.antiflood import SimpleMiddleware

# create user
db.create_table_users()

bot.setup_middleware(SimpleMiddleware(2))
if __name__ == '__main__':
    print('bot is working')
    bot.infinity_polling()
