import re
import weather

class MessageHandler:
  #класс с элементами для вывода при вводе текста, фото или документа
  #поддерживает чтение cvs exel txt json

    def __init__(self, bot):
        self.bot = bot
        self.register_handlers()


    #вывод погоды при вызове /weather
    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start_bot(message):
            self.bot.reply_to(message, f"Привет, чем могу помочь?")

        @self.bot.message_handler(commands=['help'])
        def help_bot(message):
            self.bot.reply_to(message,'Что же я могу? Я не помогу с ооп...:(\n'
                         'но я могу:\n <привет> попреветствовать вас\n '
                         '<скинь подкат> скинуть подкат с которым она/он будет 100 your\n'
                         '<анекдот>/<шуткани> пошутить до коликов в животе от смеха\n'
                         ' <как дела> ответиить на это вопрос\n'
                         '<хочу кушать>   дам вам совет)\n'
                         '<мне грустно> поддержу вас\n '
                         '<у меня нет мотивации>/<нет сил> дам цитату для поднятия духа\n '
                         '<что делаешь вечером> расскажу о своих планах\n '
                         '<спасибо> объяснять надо?\n'
                         '<n чисел от a до б> выведу n чисел в заданом диапозоне\n\n'
                         'Могу вывести на экран содержимое файлов txt, json,exel,csv\n'
                         'Могу прокомментировать ваше фото\n\n'
                         'При команде <weather> выведу погоду в Чите\n')


        @self.bot.message_handler(commands=['weather'])
        def handle_weather(message):
            wet_boy = weather.Weather
            #записываем температуру в переменную
            temperature = wet_boy.get_weather()
            #вывод температуры
            self.bot.reply_to(message, f"Температура в Чите {temperature}°C")
            #условие для картинки, которую отправляет бот при температуре ниже -30 (картинка из интернета)
            image = 'https://risovach.ru/upload/2018/01/mem/holod_166423984_orig_.jpg' if temperature < -30.0 else 'https://kartinkof.club/uploads/posts/2022-05/1653674245_8-kartinkof-club-p-veselie-kartinki-o-pogode-9.jpg'
            self.bot.send_photo(message.chat.id, image)

        #обработка фото
        @self.bot.message_handler(content_types=['photo'])
        def get_photo(message):
            #создаем кнопку
            from telebot import types
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Страничка Егра', url='https://t.me/BinOfEargosha'))
            # Ваше действие при получении фото здесь
            self.bot.reply_to(message, 'Конечно красиво НО арты Егора лучше!', reply_markup=markup)

        @self.bot.message_handler(func=lambda message: True)
        def handle_message_text(message):

            text = message.text.lower()
            response = ""

            # 1
            if re.search(r'привет|hi',  text):
                response += f'Приветствую , {message.from_user.first_name} {message.from_user.last_name}\n'
            # 2
            if re.search(r'скинь подкат',  text):
                response += 'Я не вор, но тебя бы похитил❤️'
            # 3
            if re.search('пока|прощай мой друг',  text):
                response += 'Пока, котик❤️'
            # 4
            if re.search('анекдот|шуткани',  text):
                response += 'Черепашки—ниндзя нападали вчетвером на одного, потому что у них тренер был крыса'
            # 5
            if re.search('как дела|как дела\\s|как ты\\s', text):
                response += 'все хорошо, хочу спать '
            # 6
            if re.search('хочу кушать|хочу кушать\\s',  text):
                response += 'поищи что-нибудь в холодильнике. на край есть крыса. '
            # 7
            if re.search('кто лучший(оппа|оппа\\s)', text):
                response += 'Дживайпииии~~~~'
            # 8
            if re.search('мне грустно|грустно', text):
                response += 'если вам грустно, то посмотрите видео с котиками -> https://youtu.be/l9LVcOC84wo?si=EK35kBCZfPiv6aUX'
            # 9
            if re.search('у меня нет мотивации|нет сил|я бессилен|я бессильна',  text):
                response += 'Весь мир это кастрюля, а ты лишь прилипший ко дну рис.\n Не грусти, его тоже едят '
            # 10
            if re.search('что делаешь (вечером|вечером\\s)', text):
                response += 'Сплю :0'
            # 11
            if re.search('спасибо|благодарю', text):
                response += 'Пожалуйста, котик'
            # 12
            if re.search('спс|чд|кд|крч', text):
                response += 'Тебе подарить словарь?'

            # вывод рандомных чисел в диапозоне заданным пальзователем
            if re.search(r"(\d+)\s+[числа|цифр]+\s+[от]+\s(\d+)\sдо\s(\d+)",  text):
                requested = re.search(r"(\d+)\s+[чисел|цифр|числа]+\s+[от]+\s(\d+)\sдо\s(\d+)",  text)
                n = int(requested.group(1))  # количество цифр
                a = int(requested.group(2))  # диапозон
                b = int(requested.group(3))
                import random
                result = [(random.randint(a, b)) for i in range(n)]
                if result:
                    response += f"Случайные числа: "
                    for num in result:
                        response += f"{num:3.0f}, "
            if not response:
                response = "Что-то на китайском:) Повторите пж"

            self.bot.reply_to(message, response)

        @self.bot.message_handler(content_types=['document'])
        def handle_attached_document(message):
            '''
            handle_attached_document - Обработчик для вложенных документов.
            Определяет тип файла и вызывает соответствующую функцию для обработки.
            '''
            file_info = self.bot.get_file(message.document.file_id)
            downloaded_file = self.bot.download_file(file_info.file_path)

            import pandas
            import json
            from io import BytesIO
            mime_type = message.document.mime_type

            def process_plain_text():
                '''
                 process_plain_text - Обрабатывает текстовые файлы. Декодирует
                 байтовые данные в строку и отправляет содержимое файла в ответе.
                '''
                fileС = downloaded_file.decode("utf-8")
                self.bot.reply_to(message, f"Содержимое файла (txt):\n{fileС}")

            def process_json():
                '''
                 process_json - Обрабатывает файлы JSON. Декодирует
                 байтовые данные в JSON и отправляет содержимое файла в ответе
                '''
                fileС = json.loads(downloaded_file)
                self.bot.reply_to(message, f"Содержимое файла (json):\n{fileС}")

            def process_excel():
                '''
                 process_excel - Обрабатывает файлы Excel. Использует модуль pandas для
                 чтения файла Excel из байтовых данных и отправляет содержимое файла в ответе.
                 '''
                import pandas as pd
                # Предположим, что downloaded_file содержит байтовые данные файла Excel
                # Нужно использовать BytesIO для обертывания байтовых данных
                excel_data = BytesIO(downloaded_file)

                # Теперь можно использовать excel_data вместо downloaded_file
                df = pd.read_excel(excel_data)
                #df = pandas.read_excel(downloaded_file)
                self.bot.reply_to(message, f"Содержимое файла (excel):\n{df.to_string(index=False)}")

            def process_csv():
                '''
                 process_csv - Обрабатывает файлы CSV. Декодирует байтовые данные в строку и использует модуль
                 pandas для чтения файла CSV, затем отправляет содержимое файла в ответе.
                '''
                import io
                df = pandas.read_csv(io.StringIO(downloaded_file.decode('utf-8')))
                self.bot.reply_to(message, f"Содержимое файла (CSV):\n{df.to_string(index=False)}")

            def process_unknown():
                '''
                process_unknown - Возвращает
                 сообщение об ошибке для неизвестных типов файлов
                '''
                self.bot.reply_to(message, f"Бяку в меня не суй, не знаю я этого")

            switch = {
                "text/plain": process_plain_text,
                "application/json": process_json,
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": process_excel,
                "text/csv": process_csv
            }

            switch.get(mime_type, process_unknown)()

