import sqlite3

@bot.message_hander(commands=['бибика'])
def start(message):
    # новый объект-> библиотека ->файл
    conn = sqlite3.connect('bibika.sql')
    # объект для работы с бд
    cur = conn.cursor()

    #создаем таблицу с пользователями