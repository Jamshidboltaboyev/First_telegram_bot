import telebot
import datetime
token = << Your bot api >>
bot = telebot.TeleBot(token)
#bot.send_message(1260770782, "salom bot")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f"Salom {message.from_user.first_name}")
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row('Sana', 'Soat')
    markup.row('Yangi yilga qancha qoldi')
    bot.send_message(message.from_user.id, "Bittasini tanlang...", reply_markup=markup)
@bot.message_handler(content_types = 'text')
def send_if(message):
    if message.text == 'Sana':
        sana = datetime.date.today()
        sana = str(sana)[8:]
        bot.send_message(message.from_user.id,f"Bugun : {sana} - dekabr")

    elif message.text == 'Soat':
        soat = datetime.datetime.today()
        soat = (str(soat)[11:])[:5]
        bot.send_message(message.from_user.id,f"Soat : {soat}")
    elif message.text == 'Yangi yilga qancha qoldi':
        qolgan_kun = datetime.date.today()
        qolgan_kun = 31 - int(str(qolgan_kun)[8:])
        qolgan_soat = datetime.datetime.today()
        qolgan_soat = 24 - int((str(qolgan_soat)[11:])[:2])
        qolgan_daqiqa = datetime.datetime.today()
        qolgan_daqiqa = 60 - int((str(qolgan_daqiqa)[14:])[:2])
        bot.send_message(message.from_user.id, f"Yangi yilga {qolgan_kun} kun, {qolgan_soat} soat, {qolgan_daqiqa} daqiqa qoldi")
    else:
        bot.send_message(message.from_user.id, "Uzr bunday buyruq yo'q !!!")

bot.polling(none_stop=True)
