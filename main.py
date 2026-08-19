import os
import telebot
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Estou vivo!"

def run():
    port = int(os.environ.get('PORT', 1000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = '8987294800:AAHvyJArQN2Bre50dJ1ilmfsD-PLGqDPm-w'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "O bot está online!")

keep_alive()
bot.polling()

