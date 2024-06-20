import telebot

# إدراج رمز بوت Telegram الخاص بك هنا
bot = telebot.TeleBot("6212880527:AAGIf6iLixGgcj1WuTk8u-ltpNEsc5pB1yg")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "مادارا يحبك.")

bot.polling()