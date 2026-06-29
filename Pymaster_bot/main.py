import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database.db import create_db

from handlers.settings import router as settings_router
from handlers.start import router as start_router
from handlers.learning import router as learning_router
from handlers.lessons import router as lessons_router
from handlers.practice import router as practice_router
from handlers.profile import router as profile_router
from handlers.quiz import router as quiz_router
from handlers.snake import router as snake_router
from handlers.python_runner import router as python_runner_router
from handlers.ai_assistant import router as ai_assistant_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def main():
    await create_db()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(settings_router)
    dp.include_router(start_router)
    dp.include_router(learning_router)
    dp.include_router(lessons_router)
    dp.include_router(practice_router)
    dp.include_router(profile_router)
    dp.include_router(quiz_router)
    dp.include_router(snake_router)
    dp.include_router(python_runner_router)
    dp.include_router(ai_assistant_router)

    print("🚀 BOT STARTED")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
