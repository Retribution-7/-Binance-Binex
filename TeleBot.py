import telebot
from telebot import types
import Binance


bot = telebot.TeleBot('6310108587:AAH6w1ZDo-4z-MrvZTZb-IoYfvliY68f-ug')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    binance = types.InlineKeyboardButton('BINANCE', callback_data="binance")
    bynex = types.InlineKeyboardButton('BYNEX', callback_data="bynex")
    markup.add(bynex, binance)
    bot.send_message(message.chat.id, 'Привет, в каком сервисе вы хотели бы посмотреть курс?', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    markup = types.InlineKeyboardMarkup()
    bitcoin = types.InlineKeyboardButton("BITCOIN", callback_data="binance_bitcoin")
    ethereum = types.InlineKeyboardButton("ETHEREUM", callback_data="binance_ethereum")
    bnb = types.InlineKeyboardButton("BNB", callback_data="binance_bnb")
    ripple = types.InlineKeyboardButton("RIPPLE", callback_data="binance_ripple")
    markup.row(bitcoin, ethereum)
    markup.row(bnb, ripple)
    
    
    if callback.data == 'binance':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Выберите валюту", reply_markup=markup)
        
    if callback.data == 'binance_bitcoin':
        bot.send_message(callback.message.chat.id, '1 BITCOIN = {}'.format(Binance.binance_bitcoin_price()))
        
    if callback.data == 'binance_ethereum':
        bot.send_message(callback.message.chat.id, '1 ETHEREUM = {}'.format(Binance.binance_ethereum_price()))
                         
    if callback.data == 'binance_bnb':
        bot.send_message(callback.message.chat.id, '1 BNB = {}'.format(Binance.binance_BNB_price()))
        
    if callback.data == 'binance_ripple':
        bot.send_message(callback.message.chat.id, '1 RIPPLE = {}'.format(Binance.binance_ripple_price()))

    
bot.polling(none_stop=True)
