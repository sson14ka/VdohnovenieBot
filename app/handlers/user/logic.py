from aiogram import types
from archive.app.keyboards.kbs import app_keyboard
from app.bot.utils.utils import greet_user, get_about_us_text
from app.api.dao import UserDAO

async def handle_start(message: types.Message):
    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)

    if not user:
        await UserDAO.add(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username
        )

    await greet_user(message, is_new_user=not user)

async def handle_about_us(message: types.Message):
    kb = app_keyboard(user_id=message.from_user.id, first_name=message.from_user.first_name)
    await message.answer(get_about_us_text(), reply_markup=kb)

async def handle_back(message: types.Message):
    await greet_user(message, is_new_user=False)
