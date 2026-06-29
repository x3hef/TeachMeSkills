from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lesson_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀ Назад", callback_data="back_lessons"),
            InlineKeyboardButton(text="✅ Понятно", callback_data="understood"),
        ],
        [
            InlineKeyboardButton(text="⭐ Практика", callback_data="practice_variables"),
            InlineKeyboardButton(text="▶ Следующий", callback_data="next_lesson"),
        ],
        [
            InlineKeyboardButton(
                text="📘 Документация",
                url="https://docs.python.org/3/tutorial/introduction.html"
            ),
            InlineKeyboardButton(
                text="🎥 Видео",
                url="https://www.youtube.com/results?search_query=python+переменные+для+начинающих"
            ),
        ],
    ]
)