import datetime
import telebot
#from telebot.ext import CommandHandler, Updater

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a bot. Use the /time command to know the current time.")

def get_time(update, context):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"The current time is {current_time}.")

def main():
    Updater = updater('6271547668:AAF0WGbE6lXGTBM3oSK_OrEQRVEyCWZOY80')  # замените 'TOKEN' на токен вашего бота
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    time_handler = CommandHandler('time', get_time)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(time_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
