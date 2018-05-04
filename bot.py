import telebot
TOKEN = '584948231:AAE3yBu1wBn6YBW534HqyG019Uq14yZDvKY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id,'ура! я родился')

#@bot.message_handler(regexp = 'спойлер')
#def hate(message):
#	bot.send_message(message.chat.id,'DS-лучше')

@bot.message_handler(func = lambda message:True)
def kek(message):
	if message.text == 'как фильм':
	    bot.send_message(message.chat.id,'гомора умрет')
	elif  message.text == 'хватит спойлерить':
		    bot.send_message(message.chat.id, 'и паук тоже')
	elif message.text == 'ds или marvel':
		bot.send_message(message.chat.id,'канеш марвел')
		


if __name__ == '__main__':
	bot.polling()