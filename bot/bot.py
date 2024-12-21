import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import API_TOKEN
from handlers import cmd_start, handle_message, process_contact_manager, process_continue_chat

# логирование
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)


dp = Dispatcher() 


dp.message.register(cmd_start, Command("start"))
dp.message.register(handle_message)  
dp.callback_query.register(lambda callback_query: process_contact_manager(callback_query, bot), lambda c: c.data == "contact_manager") 
dp.callback_query.register(process_continue_chat, lambda c: c.data == "continue_chat")  


async def on_start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(on_start()) 