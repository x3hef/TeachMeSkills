from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from content.lessons_data import LESSONS

roadmap_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🐍 Основы Python",
                callback_data="section_basics",
            )
        ],
        [
            InlineKeyboardButton(
                text="📦 Коллекции",
                callback_data="section_collections",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ Функции и файлы",
                callback_data="section_functions",
            )
        ],
        [
            InlineKeyboardButton(
                text="🏛️ ООП",
                callback_data="section_oop",
            )
        ],
        [
            InlineKeyboardButton(
                text="🏆 Прогресс",
                callback_data="progress",
            )
        ],
        [
            InlineKeyboardButton(
                text="🧠 Quiz",
                callback_data="quiz",
            )
        ],
    ]
)

BASICS_LESSONS = [
    "variables",
    "types",
    "strings",
    "numbers",
    "input_output",
    "conditions",
    "logic",
    "for_loop",
    "while_loop",
]

COLLECTIONS_LESSONS = [
    "lists",
    "dicts",
    "tuples_sets",
]

FUNCTIONS_LESSONS = [
    "functions",
    "modules",
    "files",
    "exceptions",
]

OOP_LESSONS = [
    "oop_basics",
    "classes_objects",
    "inheritance",
]


def make_lessons_keyboard(lesson_keys: list[str], completed: set[str]):
    keyboard = []

    for index, lesson_key in enumerate(lesson_keys, start=1):
        if lesson_key not in LESSONS:
            continue

        lesson = LESSONS[lesson_key]
        title = lesson["title"]

        if lesson_key in completed:
            status = "✅"
        else:
            status = "⭐"

        keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"{status} {index}. {title}",
                    callback_data=f"lesson_{lesson_key}",
                )
            ]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                text="⬅ Назад",
                callback_data="back_roadmap",
            )
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def get_basics_keyboard(completed: set[str]):
    return make_lessons_keyboard(
        BASICS_LESSONS,
        completed,
    )


def get_collections_keyboard(completed: set[str]):
    return make_lessons_keyboard(
        COLLECTIONS_LESSONS,
        completed,
    )


def get_functions_keyboard(completed: set[str]):
    return make_lessons_keyboard(
        FUNCTIONS_LESSONS,
        completed,
    )


def get_oop_keyboard(completed: set[str]):
    return make_lessons_keyboard(
        OOP_LESSONS,
        completed,
    )
