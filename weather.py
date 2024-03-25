import json
import requests

class Weather:
    '''
        @staticmethod - Декоратор, указывающий, что
        метод get_weather является статическим и может
        вызываться на уровне класса без создания экземпляра класса

       '''
    @staticmethod

    def get_weather():
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Chita&appid=876f9b02c8b78fa64b611c823251e1ff&units=metric')
        '''
        Отправка GET-запроса к API OpenWeatherMap для 
        получения данных о погоде в городе Chita. 
        Запрос возвращает данные в формате JSON
        '''
        # проверка успешности запроса
        if res.status_code == 200:
            #декодирование json-ответа от сервера в объект Python
            data = json.loads(res.text)
            #взятие данных
            temp = data['main']['temp']
            return temp
