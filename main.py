import telebot
from Addition import MessageHandler

# токен бота
bot = telebot.TeleBot('6896488946:AAG4sOBOn09FggQLS7hgMEhiF8s6gZjIX8I')

# Инициализируем класс обработчиков сообщений
message_handler = MessageHandler(bot)

# Запуск бота
bot.polling()
