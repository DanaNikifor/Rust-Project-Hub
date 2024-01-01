import telebot, settings, main_function

bot = telebot.TeleBot(settings.token)

print(main_function.main(int(input())))

#bot.polling(none_stop=True)