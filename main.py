import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6396880751:AAH47EDqmFYNcR9f1na2Ob6dM9yyXWEOwXY'
bot = telebot.TeleBot(bot_token)

# Start message
start_message = ("Привет, хочешь делать деньги на крипте? Тогда тебе сюда. "
                 "Здесь я дам сигналы и аналитику по крипторынку, или проще - "
                 "покажу как на ней сейчас заработать, попробовать можешь уже сейчас, "
                 "выбор делай сам, доступ бесплатный до 15.12.2023 а дальше сам решишь надо тебе или нет.")

# Menu buttons
channels_button = types.KeyboardButton('Channels')
profile_button = types.KeyboardButton('Profile')
referral_button = types.KeyboardButton('Referal')
info_button = types.KeyboardButton('Info')

# Channels submenu buttons
paid_button = types.KeyboardButton('payed')
info_channel_button = types.KeyboardButton('infochannel')

# Create main menu
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(channels_button, profile_button, referral_button, info_button)

# Create channels submenu
channels_submenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
channels_submenu.add(paid_button, info_channel_button)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, start_message, reply_markup=main_menu)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'Channels':
        bot.send_message(message.chat.id, 'Choose a channel:', reply_markup=channels_submenu)
    elif message.text == 'infochannel':
        bot.send_message(message.chat.id, 'Redirecting to info channel: https://t.me/cryptodosugchannel')
    elif message.text == 'payed':
        markup = types.InlineKeyboardMarkup()
        trial_button = types.InlineKeyboardButton('Trial 15 days', url='https://t.me/+sjE1j3Nx7KIxNTZi')
        unlim_button = types.InlineKeyboardButton('Unlim', url='https://t.me/RolXCoin')
        markup.add(trial_button, unlim_button)
        bot.send_message(message.chat.id, 'Choose an option:', reply_markup=markup)
    elif message.text == 'Profile':
        bot.send_message(message.chat.id, 'This is your profile.')
    elif message.text == 'Referal':
        bot.send_message(message.chat.id, 'This is the referral section.')
    elif message.text == 'Info':
        bot.send_message(message.chat.id, 'This is the info section.')

bot.polling(none_stop=True)
