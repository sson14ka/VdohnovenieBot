# app/bot/create_bot.py

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from app.config import settings
import logging
import aiogram

# Инициализация бота
bot = Bot(token=settings.BOT_API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# Функции для старта и остановки бота
async def start_bot():
    logging.info("Bot is starting...")
    # Здесь можно добавить логику для старта, если нужно, например, подключение к API
    logging.info("Bot started successfully.")

async def stop_bot():
    logging.info("Bot is stopping...")
    await bot.close()
    logging.info("Bot stopped.")
