import os
import telebot
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "O bot está online!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = '8987294800:AAHvyJArQN2Bre50dJ1ilmfsD-PLGqDPm-w'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "O bot está online e funcionando!")

keep_alive()
bot.infinity_polling(skip_pending=True)


