import telebot
import pyowm
from telebot import apihelper

bot = telebot.TeleBot("API....")
apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

owm = pyowm.OWM('Api.....', language='ru') 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "В каком городе узнать погоду?")


@bot.message_handler(content_types=['text'])
def echo_all(message):
	#bot.reply_to(message, message.text)
    place = message.text
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    temp = "В городе " + place + " сейчас " + str(w.get_temperature('celsius')["temp"]) + " градусов!"
    bot.send_message(message.chat.id, temp)

bot.polling( none_stop = True ) 