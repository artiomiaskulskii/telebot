from config import *
print(token)
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    reply_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_keyboard_markup.row(KeyboardButton("Start MiniApp", web_app=WebAppInfo(WEB_URL)))

    inline_keyboard_markup = InlineKeyboardMarkup()
    inline_keyboard_markup.row(InlineKeyboardButton('Start MiniApp', web_app=WebAppInfo(WEB_URL)))

    bot.reply_to(message, "Click the bottom inline button to start MiniApp", reply_markup=inline_keyboard_markup)
    bot.reply_to(message, "Click keyboard button to start MiniApp", reply_markup=reply_keyboard_markup)

@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    bot.reply_to(message, f'Your message is "{message.web_app_data.data}"')

bot.infinity_polling()