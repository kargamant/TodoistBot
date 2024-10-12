from aiogram import Bot, Dispatcher, filters
from aiogram.types import Message
from .tg_configs import TOKEN
from asyncio import run
from src.backend.oauth import URL

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(filters.CommandStart)
async def start_message(message: Message) -> None:
    reply = f"Hi! I'm your personal ai productivity assistant.\n" \
            f"To let me analyze your Todoist bin, you have to authorize.\n\n" \
            f"To authorize go via this link {URL}\n\n" \
            f"We will not use it for illegal purposes. Only for helping you to increase you productivity." #mb add ai response
    await message.answer(reply)
