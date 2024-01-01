import telebot

token = "5834288580:AAFMzPdkQmwkI9pXwMKZqmJLq_S8nPue8q4"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(massage):
	bot.send_message(massage.chat.id, '<b>Добро Пожаловать!</b>', parse_mode='html')

@bot.message_handler()
def massage_reader(massage):
	if(massage.text == "Привет" or "привет" or "прив" or "Прив"):
		bot.send_message(massage.chat.id, f"Привет, {massage.from_user.first_name}")

bot.polling(none_stop=True)