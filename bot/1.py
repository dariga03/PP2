import telebot
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


#BOT_TOKEN = “6271547668:AAF0WGbE6lXGTBM3oSK_OrEQRVEyCWZOY80” 
bot = telebot.TeleBot('6271547668:AAF0WGbE6lXGTBM3oSK_OrEQRVEyCWZOY80')

token = '6271547668:AAF0WGbE6lXGTBM3oSK_OrEQRVEyCWZOY80'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)

    await message.answer(respponse['choices'][0]['text'])

    executor.start_polling(dp, skip_updates=True)





# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     mess= f'привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#     #bot.reply_to(message, "Hello, how are you doing?")

# bot.polling(none_stop=True)   


