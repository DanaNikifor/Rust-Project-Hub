import telebot
from telebot import types
import Token

bot = telebot.TeleBot(Token.TOKEN)

@bot.message_handler(commands=['start'])
def start(massage):
	mp = types.ReplyKeyboardMarkup()
	mp.add((types.KeyboardButton("Поздороваться")))
	welcome = f"Добро Пожаловать, {massage.from_user.first_name}!"
	bot.send_message(massage.chat.id, welcome, parse_mode='html', reply_markup=mp)

@bot.message_handler()
def massage_reader(massage):
	if(massage.text in ("Привет", "привет", "прив", "Прив", "Поздороваться")):
		bot.send_message(massage.chat.id, f"Привет, {massage.from_user.first_name}")
	else:
		bot.send_message(massage.chat.id, f"😠{massage.from_user.first_name}, используй кнопочки")
	print(massage.text)

while True:
	bot.polling() 