from aiogram import types
from archive.app.keyboards.kbs import admin_keyboard
from app.config import settings

async def welcome_admin(message: types.Message):
    return await message.answer(
        f"Здравствуйте, <b>{message.from_user.full_name}</b>!\n\n"
        "Добро пожаловать в панель администратора. Здесь вы можете:\n"
        "• Просматривать все текущие заявки\n"
        "• Зарегистрировать новых пользователей\n"
        "• Анализировать статистику\n\n"
        "Для доступа к полному функционалу, пожалуйста, перейдите по ссылке ниже.\n"
        "Мы постоянно работаем над улучшением и расширением возможностей панели.",
        reply_markup=admin_keyboard(user_id=message.from_user.id)
    )
