from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Учиться"),
            KeyboardButton(text="🧠 Quiz"),
        ],
        [
            KeyboardButton(text="🐍 Змейка"),
            KeyboardButton(text="🕹️ PyRunner"),
        ],
        [
            KeyboardButton(text="🤖 AI Помощник"),
            KeyboardButton(text="🏆 Прогресс"),
        ],
        [
            KeyboardButton(text="⚙️ Настройки"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие 👇",
)
