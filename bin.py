import telebot,requests
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

def bin_info(bin):
    url = "https://lookup.binlist.net/"+bin
    try:
        r = requests.get(url).json()
        scheme = r["scheme"]
        type = r["type"]
        prepaid = r["prepaid"]
        country = r["country"]["name"] + r["country"]["emoji"]
        bank = str(r["bank"])
        msg = f"Bin: <code>{bin}</code>\nscheme: <code>{scheme}</code>\ntype: <code>{type}</code>\npreparid: <code>{prepaid}</code>\ncountry: <code>{country}</code>\nbank: <code>{bank}</code>"
        return msg
    except:
        return "Incorrect BIN"


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,f'Hello {message.from_user.first_name}\ntype /bin xxxxx to get your bin info')
@bot.message_handler(commands=['bin'])
def bin(message):
    bin = message.text.replace('/bin','').strip()
    if bin.isdigit() and len(bin) >=6:
        bot.send_message(message.chat.id,text=bin_info(bin),parse_mode='HTML',reply_markup=types.InlineKeyboardMarkup(row_width=2).add(types.InlineKeyboardButton(text='Developer 🧑‍💻',url='https://t.me/Mf4_Tn')))
@bot.message_handler(func=lambda message:True)
def loop(message):
    bin = message.text
    if bin.isdigit() and len(bin) >=6:
        bot.send_message(message.chat.id,text=bin_info(bin),parse_mode='HTML',reply_markup=types.InlineKeyboardMarkup(row_width=2).add(types.InlineKeyboardButton(text='Developer 🧑‍💻',url='https://t.me/Mf4_Tn')))

bot.polling()