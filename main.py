import telebot
from telebot import types
import Token

bot = telebot.TeleBot(Token.TOKEN)
keys = ("Поздороваться", "Правила")

@bot.message_handler(commands=['start'])
def start(massage):
	mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
	hello = types.KeyboardButton("Поздороваться")
	guide = types.KeyboardButton("Правила")
	mp.add(hello, guide)
	welcome = f"Добро Пожаловать, {massage.from_user.first_name}!"
	bot.send_message(massage.chat.id, welcome, parse_mode='html', reply_markup=mp)

@bot.message_handler()
def massage_reader(massage):
	if(massage.text in keys):
		if massage.text == "Поздороваться":
			bot.send_message(massage.chat.id, f"Привет, {massage.from_user.first_name}")
		if massage.text == "Правила":
			bot.send_message(massage.chat.id, f"Используйте кнопочки чтобы управлять ботом")
	else:
		bot.send_message(massage.chat.id, f"😠{massage.from_user.first_name}, используй кнопочки")
	print(massage.text)

while True:
	bot.polling()
# жопа