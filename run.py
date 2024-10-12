from telegram import dp, bot
from asyncio import run

if __name__ == '__main__':
    run(dp.start_polling(bot))
