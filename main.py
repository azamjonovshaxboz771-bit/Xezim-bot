import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot faol!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

import telebot
import random
import time
from telebot import types

TOKEN = "8624018316:AAGzaEtebleymlncJmffGsLNgU7MOLTDG18"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 Signal olish", callback_data="get_signal")
    markup.add(btn)
    bot.send_message(message.chat.id, "Xush kelibsiz! Signal olish uchun tugmani bosing:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "get_signal")
def send_signal(call):
    msg = bot.send_message(call.message.chat.id, "Signal tayyorlanmoqda... ⏳")
    time.sleep(1.5)
    
    signals = ["BUY 🟢", "SELL 🔴"]
    res = random.choice(signals)
    
    bot.edit_message_text(f"Yangi signal: {res}", call.message.chat.id, msg.message_id)

bot.infinity_polling()


