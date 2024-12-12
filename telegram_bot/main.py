from dotenv import load_dotenv
import os
import telebot
from telebot import types

# Загрузка токена и данных каналов
load_dotenv()
api_token = os.environ.get('TELEGRAM_BOT_TOKEN')
channels = ['@screener_web_eng', '@screener_web_ru']  # Список каналов
custom_link = "https://stock-screener-pro.ru/auth_telegram_bot/telegram_bot_access/"  # Ссылка, которая ведет на авторизацию

# Инициализация бота
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание кнопок для подписки и проверки
    markup = types.InlineKeyboardMarkup()
    for channel in channels:
        btn_subscribe = types.InlineKeyboardButton(text=f'Subscribe to {channel}', url=f'https://t.me/{channel[1:]}')
        markup.add(btn_subscribe)
    btn_check = types.InlineKeyboardButton(text='Check subscription 🔄', callback_data='check_subscribe')
    markup.add(btn_check)
    
    # Сообщение с кнопками
    bot.send_message(
        message.chat.id,
        "Subscribe to all channels to proceed",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "check_subscribe":
        # Проверка подписки на все каналы
        not_subscribed = []
        for channel in channels:
            user_status = bot.get_chat_member(channel, call.from_user.id).status
            if user_status not in ['member', 'administrator', 'creator']:
                not_subscribed.append(channel)

        if not_subscribed:
            # Если пользователь не подписан на какие-то каналы
            bot.send_message(
                call.message.chat.id,
                f"❌ You are not subscribed to the following channels:\n" +
                "\n".join(not_subscribed) +
                "\nSubscribe to all channels to proceed."
            )
        else:
            # Если пользователь подписан на все каналы
            markup = types.InlineKeyboardMarkup()
            btn_link = types.InlineKeyboardButton(text="Go to the link 🔗", url=custom_link)
            markup.add(btn_link)
            bot.send_message(
                call.message.chat.id,
                "✅ Thanks for subscribing to all channels!\nNow you can visit the website using the link below:",
                reply_markup=markup
            )

# Запуск бота
bot.polling()
