import telebot

TOKEN = '598408500:AAGFOwerBsAg1AgmDkfFkwz7IWeN_cmT9FE'

bot = telebot.TeleBot(TOKEN)

# keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
# keyboard.row('забанить Бажиханум','разбанить Бажиханум')

# @bot.message_handler(commands = ['banForBazhihanum'])
# def ban(message):
# 	msg = bot.send_message(message.chat.id, 'голосуем, товарищи',
# 		reply_markup = keyboard)
# 	bot.register_next_step_handler(msg, ban_handler)
# def ban_handler(message):
# 	if message.text == 'забанить Бажиханум':
# 		bot.send_message(message.chat.id, 'прощай Бажика')
# 	elif message.text == 'разбанить Бажиханум':
# 		bot.send_message(message.chat.id, 'прощаю, ты мне по гроб жизни обязана')

@bot.message_handler(commands = ['getRandomFilm'])
def get_film(message):
	line_kb = telebot.types.InlineKeyboardMarkup()
	but_film = telebot.types.InlineKeyboardMarkup(text = 'Дай мне фильм, срочно!',
		callback_data = 'фильм') #создаем кнопку
	line_kb.add(my_button) #вешаем кнопку на клаву
	but_kinopoisk = telebot.types.InlineKeyboardButton(text = 'открыть кинопоиск',
		url ='https://www.kinopoisk.ru/')
	line_kb.add(but_kinopoisk)
	bot.send_message(message.chat.id, 'что будем смотреть?', reply_markup = line_kb)

@bot.callback_query_handler(func = lambda call: True)
def random_film(callobj):
	if callobj.data == 'фильм':
		bot.send_message(callobj.message.chat.id, 'властелин колец')

		
if __name__ == '__main__':
	bot.polling()