import logging
import types

from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('67ecae1b99a97b303eb167893e8da6d2', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("5141141711:AAGdzk0PPL6xeLbrcaSXwgtccEN4iGk2eMw", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, впиши в меня название города и я дам тебе актуальную погоду :)")


# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     # Добавляем две кнопки
#     markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
#     item1 = types.KeyboardButton("Питер")
#     item2 = types.KeyboardButton("Москва")
#     markup.add(item1)
#     markup.add(item2)
#     bot.send_message(m.chat.id,
#                      'Нажми: \nВыбери город для получения погоды ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    detail = w.detailed_status
    temp = w.temperature('celsius')['temp']
    wind = w.wind()['speed']
    answer = f"В городе {message.text} сейчас {detail}" + '\n'
    answer += f'Температура около {temp:.1f} по Цельсию' + '\n'
    answer += f'Ветер {wind} м/с' + '\n\n'
    if temp < -5:
        answer += 'Мороз, одевайся, как капуста!'
    elif temp < 0:
        answer += 'Ну так, не сильный мороз, но шапку не забудь :)'
    elif temp < 10:
        answer += 'Не страшно, в осенней куртке будет ок'
    elif temp < 30:
        answer += 'Че хош, то и надевай, там жесть жара'
    elif temp > 30:
        answer += 'Там гребанное пекло, не выходи.'
    bot.send_message(message.chat.id, answer)



bot.infinity_polling()
