from config import *
print(token)
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
@bot.message_handler(commands=['info','information'])
def send_information(message):
    bot.reply_to(message, """\ 
Привет! Я бот-дизайнер, и я здесь, чтобы помочь тебе с творческими задачами и идеями для дизайна. Какой у тебя проект? Вот несколько вещей, с которыми я могу помочь:
1. **Логотипы**: Нужен уникальный логотип для твоего бизнеса? Опиши свою идею, и я помогу сформировать концепцию!
2. **Цветовые палитры**: Сомневаешься в цветах? Я предложу несколько гармоничных цветовых схем, которые подойдут для твоего проекта.
3. **Шрифты**: Ищешь идеальные шрифты для своего текста? Я подскажу, какие сочетания будут выглядеть стильно и современно.
4. **Макеты**: Нужна помощь с созданием макета для веб-сайта или приложения? Я помогу с идеями по структуре и компоновке.
5. **Идеи и вдохновение**: Ищешь свежие идеи? Я могу предложить тренды в дизайне и показать успешные примеры работ.
Просто дай мне знать, что именно тебе нужно, и я постараюсь помочь!
 умею выполянть множество команд:
/start
/help
/info
\
""")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
