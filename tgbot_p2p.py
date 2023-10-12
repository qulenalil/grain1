import telebot
from telebot import types

bot = telebot.TeleBot('6502053381:AAHSKmC2EUz8nzlDbADYvLiDcQMRk3-qr_E')

@bot.message_handler(commands=['start'])
def start(message):
    qln=bot.send_message(message.chat.id,'<b>Введите сумму</b>',parse_mode='html')
    bot.register_next_step_handler(qln,func)

def func(message):
    global qln1
    qln1=message.text
    qln1=int(qln1)
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1=types.KeyboardButton('0.25 % Garantex')
    btn2=types.KeyboardButton('0.1 % Bybit')
    btn3=types.KeyboardButton('0.2 % HTX')
    btn4=types.KeyboardButton('0.1 % KuCoin')
    markup.add(btn1,btn2,btn3,btn4)
    rfh=bot.send_message(message.chat.id,text='<b>Комиссия покупки</b>',reply_markup=markup,parse_mode='html')
    bot.register_next_step_handler(rfh,buy)

def buy(message):
    global rfh1
    rfh1=message.text
    rfh1=rfh1[:4]
    rfh1=float(rfh1)
    b=bot.send_message(message.chat.id,'<b>Покупка USDT</b>',parse_mode='html')  
    bot.register_next_step_handler(b,com)
        
def com(message):
    global b1
    b1=message.text
    b1=float(b1)
    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    btn1=types.KeyboardButton('0.25 % Garantex')
    btn2=types.KeyboardButton('0.1 % Bybit')
    btn3=types.KeyboardButton('0.2 % HTX')
    btn4=types.KeyboardButton('0.1 % KuCoin')
    markup.add(btn1,btn2,btn3,btn4)
    c=bot.send_message(message.chat.id,text='<b>Комиссия продажи</b>',reply_markup=markup,parse_mode='html')
    bot.register_next_step_handler(c,sell)

def sell(message):
    global c1
    c1 = message.text
    c1=c1[:4]
    c1= float(c1)
    d=bot.send_message(message.chat.id,'<b>Продажа USDT</b>',parse_mode='html')
    bot.register_next_step_handler(d,end)

def end(message):
    global d1
    d1 = message.text
    d1=float(d1)
    k0=qln1/100*rfh1
    k=qln1-k0#сумма после комиссии
    p=k/b1#купили
    pr=p*d1#сумма после продажи
    prk=pr-(pr/100*c1)#сумма после продажи с комиссией
    ku=prk-qln1#прибыль
    sp=ku/(qln1/100)#спред
    bot.send_message(message.chat.id,f'<b>Купленное количество USDT:</b> {round(p,3)}\n<b>Сумма после продажи:</b> {round(prk,3)} ₽\n<b>Прибыль:</b> {round(ku,3)} ₽\n<b>Спред:</b> {round(sp,3)} %',parse_mode='html')

bot.polling(none_stop=True)