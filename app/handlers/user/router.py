from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.user.logic import handle_start, handle_about_us, handle_back

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Обрабатывает команду /start.
    """
    await handle_start(message)

@user_router.message(F.text == '🔙 Назад')
async def cmd_back_home(message: Message) -> None:
    """
    Обрабатывает нажатие кнопки "Назад".
    """
    await handle_back(message)

@user_router.message(F.text == "ℹ️ О нас")
async def about_us(message: Message):
    await handle_about_us(message)
