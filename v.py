import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def hi(message):
    bot.reply_to(message,"hello user")

bot.polling()