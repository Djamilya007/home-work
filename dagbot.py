import telebot

TOKEN = '598408500:AAGFOwerBsAg1AgmDkfFkwz7IWeN_cmT9FE'

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard.row('забанить Бажиханум','разбанить Бажиханум')

@bot.message_handler(commands = ['banForBazhihanum'])
def ban(message):
	bot.send_message(message.chat.id, 'голосуем, товарищи',
		reply_markup = keyboard
		)
if __name__ == '__main__':
	bot.polling()