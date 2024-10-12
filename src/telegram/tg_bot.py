from aiogram import Bot, Dispatcher, filters
from aiogram.types import Message
from .tg_configs import TOKEN
from asyncio import run

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(filters.CommandStart)
async def start_message(message: Message) -> None:
    reply = "Hi! I'm your personal ai productivity assistant." \
            "To let me analyze your Todoist bin, send me your backend token." \
            "We will not use it for illegal purposes. Only for helping you to increase you productivity." #mb add ai response
    await message.answer(reply)
