from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from content.lessons_data import LESSON_ORDER


def get_next_lesson_key(lesson_key: str) -> str | None:
    if lesson_key not in LESSON_ORDER:
        return None

    index = LESSON_ORDER.index(lesson_key) + 1

    if index >= len(LESSON_ORDER):
        return None

    return LESSON_ORDER[index]


def get_lesson_keyboard(lesson_key: str, lesson: dict):
    next_key = get_next_lesson_key(lesson_key)

    keyboard = [
        [
            InlineKeyboardButton(
                text="✅ Понятно",
                callback_data=f"understood_{lesson_key}",
            ),
            InlineKeyboardButton(
                text="⭐ Практика",
                callback_data=f"practice_{lesson_key}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧠 Quiz",
                callback_data=f"start_quiz:{lesson_key}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎥 Видео",
                url=lesson["video"],
            ),
            InlineKeyboardButton(
                text="📚 Документация",
                url=lesson["docs"],
            ),
        ],
        [
            InlineKeyboardButton(
                text="📄 Статья",
                url=lesson["article"],
            ),
        ],
    ]

    if next_key:
        keyboard.append(
            [
                InlineKeyboardButton(
                    text="▶ Следующий урок",
                    callback_data=f"lesson_{next_key}",
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                text="⬅ Назад",
                callback_data="back_lessons",
            )
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
