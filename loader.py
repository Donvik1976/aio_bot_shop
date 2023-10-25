from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

# создаем объект бота и передаем набор параметров – токен и режим форматирования сообщений, сообщение будет отправлено
# с HTML-разметкой
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Для хранения состояний между этапами взаимодействия с ботом
# MemoryStorage позволяет хранить все данные в оперативной памяти
storage = MemoryStorage()
# Создаем объект диспетчера для обработки входящих сообщений и запросов
dp = Dispatcher(bot, storage=storage)
# Создаем объект менеджера баз данных
db = DatabaseManager('data/database.db')
