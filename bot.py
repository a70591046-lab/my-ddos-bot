import telebot
import os
from flask import Flask
from threading import Thread

# 1. Render uchun kichik veb-server (uyg'oq turishi uchun)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Bot qismi
TOKEN = "BU_YERGA_TOKENINGIZNI_YOZING"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men Render-da 24/7 ishlayapman!")

# 3. Ishga tushirish
if __name__ == "__main__":
    keep_alive() # Veb-serverni yoqish
    print("Bot ishga tushdi...")
    bot.polling(none_stop=True)


