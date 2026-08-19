
import os
import telebot

TOKEN = '8987294800:AAHvyJArQN2Bre50dJ1ilm'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "O bot está online!")

bot.infinity_polling()
