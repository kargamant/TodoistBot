from aiogram import Bot, Dispatcher, filters
from aiogram.types import Message
from aiogram.utils.formatting import TextLink, Text
from .tg_configs import TOKEN
from asyncio import run
from src.backend.oauth import URL


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(filters.CommandStart)
async def start_message(message: Message) -> None:
    oauth_link = TextLink('link', url=URL)

    reply = [f"Hi! I'm your personal ai productivity assistant.\n",
            f"I'm totally ready to help you resolve all chaos in your todoist.\n\n",
            f"To let me analyze your Todoist bin, you have to authorize via todoist.\n\n",
            f"To authorize go via this ",
             oauth_link,
            f" and send token that you will see on our website\n\n"
            f"We will not use it for illegal purposes. Only for helping you to increase you productivity."] #mb add ai response
    content = Text(*reply)

    await message.answer(**content.as_kwargs())

