import telebot
import Token

bot = telebot.TeleBot(Token.TOKEN)

@bot.message_handler(commands=['start'])
def start(massage):
	bot.send_message(massage.chat.id, '<b>Добро Пожаловать!</b>', parse_mode='html')

@bot.message_handler()
def massage_reader(massage):
	if(massage.text in ("Привет", "привет", "прив", "Прив")):
		bot.send_message(massage.chat.id, f"Привет, {massage.from_user.first_name}")
	else:
		bot.send_message(massage.chat.id, f"{massage.from_user.first_name}, напиши привет")
		print(massage.text)

while True:
	bot.polling() 