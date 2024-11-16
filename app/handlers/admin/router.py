from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.admin.logic import welcome_admin

admin_router = Router()

@admin_router.message(F.text == '🔑 Админ панель', F.from_user.id.in_([settings.ADMIN_ID]))
async def admin_panel(message: Message):
    await welcome_admin(message)

@admin_router.callback_query(F.data == 'back_home')
async def cmd_back_home_admin(callback: CallbackQuery):
    await callback.answer(f"С возвращением, {callback.from_user.full_name}!")
    await callback.message.answer(
        f"С возвращением, <b>{callback.from_user.full_name}</b>!\n\n"
        "Надеемся, что работа в панели администратора была продуктивной. "
        "Если у вас есть предложения по улучшению функционала, "
        "пожалуйста, сообщите нам.\n\n"
        "Чем еще я могу помочь вам сегодня?",
        reply_markup=main_keyboard(user_id=callback.from_user.id, first_name=callback.from_user.first_name)
    )
