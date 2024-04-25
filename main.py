import telebot
import random

bot = telebot.TeleBot('7123684087:AAE-WqBzgBcdAcQyHK4uMwmfL7H6e0C55Dg');


@bot.message_handler(commands=['start'])

def kwaking(message):
    number = random.randint(0, 9)
    kwaknumber = []
    bot.send_message(message.chat.id, str(number))
    if number > 0:
        while number > 0:
            kwaknumber.append("квак ")
            number = number - 1
        kwaknumber = str(kwaknumber).replace("'", '')
        kwaknumber = str(kwaknumber).replace("[", '')
        kwaknumber = str(kwaknumber).replace("]", '')
        kwaknumber = str(kwaknumber).replace(",", '')
        bot.send_message(message.chat.id, kwaknumber)
        number = random.randint(0, 9)
    else :
        bot.send_message(message.chat.id, 'плюх')


bot.polling(none_stop=True, interval=0)