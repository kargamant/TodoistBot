from src.telegram import dp, bot
from src.database.engine import engine
from src.database.models import Base
from asyncio import run

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run(dp.start_polling(bot))
