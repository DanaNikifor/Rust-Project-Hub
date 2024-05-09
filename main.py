import telebot
from telebot import types
import Token

bot = telebot.TeleBot(Token.TOKEN)
keys = ("Поздороваться", "Правила", "Проекты", "Назад")
projectsKeys = ("Простые", "Средние", "Сложные")
ProjectsLow = ("Компиляция проекта", "Hello World", "Списки, картежи и словари")
ProjectsMednum = ("Калькулятор", "Мини игра угадай, 'что я загадал?'")
ProjectsHard = ("Крестики-нолики", "Проект на Android")

@bot.message_handler(commands=['start'])
def start(massage):
	mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
	hello = types.KeyboardButton("Поздороваться")
	projects = types.KeyboardButton("Проекты")
	mp.add(hello,projects)
	welcome = f"Добро Пожаловать, {massage.from_user.first_name}!"
	bot.send_message(massage.chat.id, welcome, parse_mode='html', reply_markup=mp)

@bot.message_handler()
def massage_reader(massage):
	if(massage.text in keys):
		if massage.text == "Поздороваться":
			bot.send_message(massage.chat.id, f"Привет, {massage.from_user.first_name}\n\nэтот бот создан для программистов на языке Rust!\nЗдесь вы можете узнать о Rust, узнать о проектах и многое другое!\n\nНажимай на кнопочки чтобы управлять ботом")
		elif massage.text == "Проекты":
			mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Low = types.KeyboardButton(projectsKeys[0])
			Mednum = types.KeyboardButton(projectsKeys[1])
			Hard = types.KeyboardButton(projectsKeys[2])
			Back = types.KeyboardButton("Назад")
			mp.add(Low, Mednum, Hard, Back)
			text = f"Выбери сложность"
			bot.send_message(massage.chat.id, text, reply_markup=mp)
		elif massage.text == "Назад":
			mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
			hello = types.KeyboardButton("Поздороваться")
			projects = types.KeyboardButton("Проекты")
			mp.add(hello,projects)
			bot.send_message(massage.chat.id, "Вы вернулись назад", parse_mode='html', reply_markup=mp)
	elif(massage.text in projectsKeys):
		if(massage.text == projectsKeys[0]):
			mpProjectLow = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Compilation = types.KeyboardButton(ProjectsLow[0])
			Hello_World = types.KeyboardButton(ProjectsLow[1])
			Lists = types.KeyboardButton(ProjectsLow[2])
			Back = types.KeyboardButton("Назад")
			mpProjectLow.add(Compilation, Hello_World, Lists, Back)
			bot.send_message(massage.chat.id, f"Выберите проект", parse_mode='html', reply_markup=mpProjectLow)
		elif(massage.text == projectsKeys[1]):
			mpProjectMednum = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Calculator = types.KeyboardButton(ProjectsMednum[0])
			MiniGame = types.KeyboardButton(ProjectsMednum[1])
			Back = types.KeyboardButton("Назад")
			mpProjectMednum.add(Calculator, MiniGame, Back)
			bot.send_message(massage.chat.id, f"Выберите проект", parse_mode='html', reply_markup=mpProjectMednum)
		elif(massage.text == projectsKeys[2]):
			mpProjectHard = types.ReplyKeyboardMarkup(resize_keyboard=True)
			TicTacToe = types.KeyboardButton(ProjectsHard[0])
			OnAndroid = types.KeyboardButton(ProjectsHard[1])
			Back = types.KeyboardButton("Назад")
			mpProjectHard.add(TicTacToe, OnAndroid, Back)
			bot.send_message(massage.chat.id, f"Выберите проект", parse_mode='html', reply_markup=mpProjectHard)
	elif(massage.text in ProjectsLow):
		if(massage.text == ProjectsLow[0]):
			with open("Projects/Low/Compilet.txt", "r", encoding='utf-8') as file:
				bot.send_message(massage.chat.id, file.read(), parse_mode="markdown")
		if(massage.text == ProjectsLow[1]):
			with open("Projects/Low/Hello_World.txt", "r", encoding='utf-8') as file:
				bot.send_message(massage.chat.id, file.read(), parse_mode="markdown")
		elif(massage.text == ProjectsLow[2]):
			with open("Projects/Low/Lists.txt", "r", encoding='utf-8') as file:
				bot.send_message(massage.chat.id, file.read(), parse_mode="markdown")
	elif(massage.text in ProjectsMednum):
		if(massage.text == ProjectsMednum[0]):
			with open("Projects/Mednum/Calculator.txt", "r", encoding='utf-8') as file:
				bot.send_message(massage.chat.id, file.read(), parse_mode="markdown")
		elif(massage.text == ProjectsMednum[1]):
			with open("Projects/Mednum/MiniGame.txt", "r", encoding='utf-8') as file:
				bot.send_message(massage.chat.id, file.read(), parse_mode="markdown")
	elif(massage.text in ProjectsHard):
		if(massage.text == ProjectsHard[0]):
			bot.send_message(massage.chat.id, "Сам учи!😠")
		elif(massage.text == ProjectsHard[1]):
			bot.send_message(massage.chat.id, "Сам учи!😠")
	else:
		bot.send_message(massage.chat.id, f"😠{massage.from_user.first_name}, используй кнопочки")
	print(massage.text)

while True:
	bot.polling()