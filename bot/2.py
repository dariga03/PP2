import sqlite3
from telegram.ext import Updater, CommandHandler

# создаем базу данных и устанавливаем соединение
conn = sqlite3.connect('C:\dori\pp2\lab.10\databased.init')
cursor = conn.cursor()

# создаем таблицу users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        phone_number TEXT,
        chat_id INTEGER
    )
''')
conn.commit()

# обработчик команд /start и /hello
def send_welcome(update, context):
    chat_id = update.message.chat_id
    username = update.message.chat.username
    phone_number = update.message.contact.phone_number if update.message.contact else None

    # проверяем, существует ли пользователь в таблице users
    cursor.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
    user = cursor.fetchone()
    if not user:
        # добавляем нового пользователя в таблицу users
        cursor.execute('INSERT INTO users (username, phone_number, chat_id) VALUES (?, ?, ?)', (username, phone_number, chat_id))
        conn.commit()

    # отправляем приветственное сообщение
    context.bot.send_message(chat_id=chat_id, text="Hello, how are you doing?")

# создаем объект Updater и регистрируем обработчики команд
updater = Updater('6271547668:AAF0WGbE6lXGTBM3oSK_OrEQRVEyCWZOY80')
updater.dispatcher.add_handler(CommandHandler(['start', 'hello'], send_welcome))

# запускаем бота
updater.start_polling()
updater.idle()

# закрываем соединение с базой данных при остановке бота
conn.close()