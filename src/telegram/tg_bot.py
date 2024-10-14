from aiogram import Bot, Dispatcher, filters
from aiogram import F
from aiogram.types import Message
from aiogram.utils.formatting import TextLink, Text
from .tg_configs import TOKEN
from src.todoist import TOKEN_LENGTH
from src.backend.oauth import URL
from src.todoist import verify_token, TodoistService
from src.database.repository import UserRepository


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(filters.CommandStart())
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


@dp.message(F.text.len() == TOKEN_LENGTH)
async def get_token(message: Message) -> None:
    if await verify_token(message.text) is False:
        await message.answer('Sorry. Your token is incorrect or expired. Try again.')
    else:
        repo = UserRepository()
        if repo.get_user_by_tg_id(message.from_user.username) is None:
            repo.register_user(message.from_user.username, message.text)
            print(repo.get_user_by_tg_id(message.from_user.username))

            reply = f"Congratilations! You are now authorized via todoist.\n\n" \
                    f"To make sure oauth was successful check your todoist inbox, I left a greeting task for you.\n\n" \
                    f"You can delete it or close if you want.\n\n" \
                    f"Now I can start reviewing your tasks and projects to help you become more productive.\n\n" \

            await message.answer(reply)
        else:
            repo.update_access_token(message.from_user.username, message.text)

            reply = f"Your access token was successfully updated dear @{message.from_user.username}."

            await message.answer(reply)
