from aiogram import types
from aiogram import Bot
from aiogram.types import CallbackQuery
from model import chat_with_bot

user_message_count = {}

manager_chat_id = 4268502969

# Функция для подсчета сообщений
def increment_user_message_count(user_id: int):
    if user_id not in user_message_count:
        user_message_count[user_id] = 0
    user_message_count[user_id] += 1


# Обработка нажатия кнопки "Связаться с менеджером"
async def process_contact_manager(callback_query: CallbackQuery, bot: Bot):
    user_id = callback_query.from_user.id

    await callback_query.answer("Администратор напишет вам")
    await bot.send_message(manager_chat_id, f"Пользователь {user_id}")



async def process_continue_chat(callback_query: CallbackQuery):
    await callback_query.answer("Задайте вопрос")



async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, помощник сервиса MpVision")



async def handle_message(message: types.Message):
    user_id = message.from_user.id
    increment_user_message_count(user_id)  

    if user_message_count[user_id] % 3 == 0:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="contact_manager"),
                types.InlineKeyboardButton(text="Продолжить чат с ботом", callback_data="continue_chat")
            ]
        ])
        await message.answer("Вы отправили больше 3 сообщений. Хотите связаться с менеджером?", reply_markup=keyboard)
    else:
        user_message = message.text
        response = chat_with_bot(user_message)  
        await message.answer(response)
