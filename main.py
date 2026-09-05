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

TOKEN = "8983987480:AAFmnZLYReOwkTwDQgCteMgUi1IY8bmNdOk"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 Signal olish", callback_data="get_signal")
    markup.add(btn)
    bot.send_message(message.chat.id, "👋 Xush kelibsiz! Signal olish uchun tugmani bosing:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "get_signal")
def send_signal(call):
    msg = bot.send_message(call.message.chat.id, "🔍 Algoritm tahlil qilmoqda...")
    time.sleep(1.5)
    
    coefficient = round(random.uniform(1.10, 3.80), 2)
    accuracy = random.randint(88, 97)

    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 Yana signal olish", callback_data="get_signal")
    markup.add(btn)

    final_text = f"🎯 **Yangi Signal!**\n\n📈 **Koeffitsient:** {coefficient}x\n🎯 **Aniqlik kuchi:** {accuracy}%\n⏱ **Tavsiya etilgan vaqt:** Hozirgi raund"
    bot.edit_message_text(final_text, call.message.chat.id, msg.message_id, parse_mode="Markdown", reply_markup=markup)

bot.infinity_polling()

