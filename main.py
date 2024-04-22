import telebot
from telebot import types
import Token

bot = telebot.TeleBot(Token.TOKEN)
keys = ("Поздороваться", "Правила", "Проекты")
projectsKeys = ("Простые", "Средние", "Сложные")
ProjectsLow = ("Hello World", "Списки, картежи и словари", "Мини игра угадай, 'что я загадал?'")
ProjectsMednum = ("Телеграм бот", "Компиляция в exe или в бинарник", "Подключение других языков в код")
ProjectsHard = ("Игра на PyGame", "Сайт с Django", "Android приложение на Python")

@bot.message_handler(commands=['start'])
def start(massage):
	mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
	hello = types.KeyboardButton("Поздороваться")
	projects = types.KeyboardButton("Проекты")
	guide = types.KeyboardButton("Правила")
	mp.add(hello,projects, guide)
	welcome = f"Добро Пожаловать, {massage.from_user.first_name}!"
	bot.send_message(massage.chat.id, welcome, parse_mode='html', reply_markup=mp)

@bot.message_handler()
def massage_reader(massage):
	if(massage.text in keys):
		if massage.text == "Поздороваться":
			bot.send_message(massage.chat.id, f"Привет, {massage.from_user.first_name}\n\nэтот бот создан для программистов на языке Python!")
		elif massage.text == "Правила":
			bot.send_message(massage.chat.id, f"Используйте кнопочки чтобы управлять ботом")
		elif massage.text == "Проекты":
			mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Low = types.KeyboardButton(projectsKeys[0])
			Mednum = types.KeyboardButton(projectsKeys[1])
			Hard = types.KeyboardButton(projectsKeys[2])
			mp.add(Low, Mednum, Hard)
			text = f"Выбери сложность"
			bot.send_message(massage.chat.id, text, reply_markup=mp)
	elif(massage.text in projectsKeys):
		if(massage.text == projectsKeys[0]):
			bot.send_message(massage.chat.id, f"{ProjectsLow[0]}\n\n{ProjectsLow[1]}\n\n{ProjectsLow[2]}")
		elif(massage.text == projectsKeys[1]):
			bot.send_message(massage.chat.id, f"{ProjectsMednum[0]}\n\n{ProjectsMednum[1]}\n\n{ProjectsMednum[2]}")
		elif(massage.text == projectsKeys[2]):
			bot.send_message(massage.chat.id, f"{ProjectsHard[0]}\n\n{ProjectsHard[1]}\n\n{ProjectsHard[2]}")
	else:
		bot.send_message(massage.chat.id, f"😠{massage.from_user.first_name}, используй кнопочки")
	print(massage.text)

while True:
	bot.polling()