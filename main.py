import telebot
from telebot import types
import Token

bot = telebot.TeleBot(Token.TOKEN)
keys = ("Поздороваться", "Правила", "Проекты", "Назад")
projectsKeys = ("Простые", "Средние", "Сложные")
ProjectsLow = ("Hello World", "Списки, картежи и словари", "Мини игра угадай, 'что я загадал?'")
ProjectsMednum = ("Телеграм бот", "Компиляция в Python", "Подключение других ЯП")
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
			Back = types.KeyboardButton("Назад")
			mp.add(Low, Mednum, Hard, Back)
			text = f"Выбери сложность"
			bot.send_message(massage.chat.id, text, reply_markup=mp)
		elif massage.text == "Назад":
			mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
			hello = types.KeyboardButton("Поздороваться")
			projects = types.KeyboardButton("Проекты")
			guide = types.KeyboardButton("Правила")
			mp.add(hello,projects, guide)
			bot.send_message(massage.chat.id, "Вы вернулись назад", parse_mode='html', reply_markup=mp)
	elif(massage.text in projectsKeys):
		if(massage.text == projectsKeys[0]):
			mpProjectLow = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Hello_World = types.KeyboardButton(ProjectsLow[0])
			List = types.KeyboardButton(ProjectsLow[1])
			Guess = types.KeyboardButton(ProjectsLow[2])
			Back = types.KeyboardButton("Назад")
			mpProjectLow.add(Hello_World, List, Guess, Back)
			bot.send_message(massage.chat.id, f"Выберите проект", parse_mode='html', reply_markup=mpProjectLow)
		elif(massage.text == projectsKeys[1]):
			mpProjectMednum = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Telegram = types.KeyboardButton(ProjectsMednum[0])
			Compilation = types.KeyboardButton(ProjectsMednum[1])
			Other_languages = types.KeyboardButton(ProjectsMednum[2])
			Back = types.KeyboardButton("Назад")
			mpProjectMednum.add(Telegram, Compilation, Other_languages, Back)
			bot.send_message(massage.chat.id, f"Выберите проект", parse_mode='html', reply_markup=mpProjectMednum)
		elif(massage.text == projectsKeys[2]):
			mpProjectHard = types.ReplyKeyboardMarkup(resize_keyboard=True)
			Pygame = types.KeyboardButton(ProjectsHard[0])
			Django = types.KeyboardButton(ProjectsHard[1])
			Android = types.KeyboardButton(ProjectsHard[2])
			Back = types.KeyboardButton("Назад")
			mpProjectHard.add(Pygame, Django, Android, Back)
			bot.send_message(massage.chat.id, f"Выберите проект", parse_mode='html', reply_markup=mpProjectHard)
	elif(massage.text in ProjectsLow):
		if(massage.text == ProjectsLow[0]):
			bot.send_message(massage.chat.id, "Самая первая программа на языке Python:\n\n```python\nprint('Hello World')```", parse_mode="markdown")
		elif(massage.text == ProjectsLow[1]):
			bot.send_message(massage.chat.id, "Базовые коллекции в Python:\n\nСписки (lists)\n```python\nlist = [1, 2, 3, 4, 5]\nprint(list)\n```\nКортежи (tuples)(в отличие от списков, кортежи неизменяемы)\n```python\ntuple = (1, 2, 3, 4, 5)\nprint(tuple)\n```\nСловари (dictionaries)\n```python\ndictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}\nprint(dictionary)\n```", parse_mode="markdown")
		elif(massage.text == ProjectsLow[2]):
			bot.send_message(massage.chat.id, "Мини игра угадай, 'что я загадал?'\n\n```python\nimport random\n\ndef main():\n	# Генерируем случайное число от 1 до 10\n    number = random.randint(1, 10)\n\n    # Даем пользователю три попытки угадать число\n    for i in range(3):\n        user_number = int(input('Введите число: '))\n        if user_number == number:\n            print('Ты выйграл!')\n            break\n        else:\n            print(f'Неверно, у тебя осталось {3 - i - 1} попыток')\n\nif __name__ == '__main__':\n    main()\n```", parse_mode="markdown")
	elif(massage.text in ProjectsMednum):
		if(massage.text == ProjectsMednum[0]):
			bot.send_message(massage.chat.id, "Код для базового телеграм бота:\n\n```python\nimport telebot\n\nTOKEN = 'Токен_из_Bot_Father'\n\nbot = telebot.TeleBot(TOKEN)\n\n@bot.message_handler(commands=['start'])\ndef start(massage):\n    bot.send_message(massage.chat.id, 'Привет, я телеграм бот!')\n\nif __name__ == '__main__':\n    bot.polling()\n```", parse_mode="markdown")
		if(massage.text == ProjectsMednum[1]):
			bot.send_message(massage.chat.id, "Компиляция в Python через pyinstaller:\n(Linux)\n```bash\npyinstaller -F имя_файла.py\n```\n(Windows)\n```bash\npyinstaller -F имя_файла.py\n```\nГде `имя_файла.py` - это имя файла который вы хотите скомпилировать,\n\n-F - это флаг который говорит о том что мы хотим создать один файл\n\nили через auto-py-to-exe(его надо только скачать и запустить)", parse_mode="markdown")
		if(massage.text == ProjectsMednum[2]):
			bot.send_message(massage.chat.id, "Подключение других ЯП(На пример C++ на Windows):\n\nПишем библиотеку на C++:\n```cpp\n#include <iostream>\nusing namespace std;\n\nvoid printHello() {\n    cout << \"Hello C++\" << \"\\n\"\n}```\nКомпилируем:```bash\ng++ название_файла_C++ -o название_для_библеотеки.dll```\n\nИмпортируем библиотеку в Python:\n```python\nimport ctypes\nlib = ctypes.CDLL('назвыние_библиотеки_C++.dll')\nlib.printHello()\n```", parse_mode="markdown")
	elif(massage.text in ProjectsHard):
		if(massage.text == ProjectsHard[0]):
			bot.send_message(massage.chat.id, "")
		if(massage.text == ProjectsHard[1]):
			bot.send_message(massage.chat.id, "")
		if(massage.text == ProjectsHard[2]):
			bot.send_message(massage.chat.id, "")
	else:
		bot.send_message(massage.chat.id, f"😠{massage.from_user.first_name}, используй кнопочки")
	print(massage.text)

while True:
	bot.polling()