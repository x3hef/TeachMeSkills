from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from content.quizzes import QUIZZES
from database.requests import add_xp

router = Router()

# Временное хранение прогресса квиза в памяти.
# Для текущего бота этого достаточно. Позже можно перенести в БД.
user_quiz_state: dict[int, dict[str, int | str | set[int]]] = {}


def build_quiz_keyboard(lesson_key: str, question_index: int) -> InlineKeyboardMarkup:
    question = QUIZZES[lesson_key][question_index]

    buttons = []
    for answer_index, answer_text in enumerate(question["a"]):
        buttons.append([
            InlineKeyboardButton(
                text=answer_text,
                callback_data=f"quiz_answer:{lesson_key}:{question_index}:{answer_index}",
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_quiz_title(lesson_key: str) -> str:
    titles = {
        "variables": "Переменные",
        "types": "Типы данных",
        "strings": "Строки",
        "numbers": "Числа",
        "input_output": "Ввод / вывод",
        "conditions": "Условия",
        "logic": "Логика",
        "for_loop": "Цикл for",
        "while_loop": "Цикл while",
        "functions": "Функции",
        "lists": "Списки",
        "dicts": "Словари",
        "tuples_sets": "Кортежи и множества",
        "exceptions": "Исключения",
        "files": "Файлы",
        "modules": "Модули",
        "oop_basics": "ООП основы",
        "classes_objects": "Классы и объекты",
        "inheritance": "Наследование",
    }
    return titles.get(lesson_key, lesson_key)


async def send_quiz_question(message: Message, lesson_key: str, question_index: int):
    question = QUIZZES[lesson_key][question_index]
    total = len(QUIZZES[lesson_key])

    await message.answer(
        f"🧠 <b>QUIZ · {get_quiz_title(lesson_key)}</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"<b>Вопрос {question_index + 1} / {total}</b>\n"
        f"{question['q']}\n\n"
        "Выбери правильный ответ 👇",
        parse_mode="HTML",
        reply_markup=build_quiz_keyboard(lesson_key, question_index),
    )


async def start_quiz_for_user(message: Message, user_id: int, lesson_key: str = "variables"):
    if lesson_key not in QUIZZES:
        await message.answer("❌ Для этого урока квиз пока не добавлен.")
        return

    user_quiz_state[user_id] = {
        "lesson": lesson_key,
        "question_index": 0,
        "correct_answers": 0,
        "answered": set(),
    }

    await send_quiz_question(message, lesson_key, 0)


@router.message(F.text == "🧠 Quiz")
async def start_quiz_from_main_menu(message: Message):
    await start_quiz_for_user(message, message.from_user.id, "variables")


@router.message(F.text.lower() == "quiz")
async def start_quiz_from_text(message: Message):
    await start_quiz_for_user(message, message.from_user.id, "variables")


@router.callback_query(F.data == "quiz")
async def start_quiz_from_inline(callback: CallbackQuery):
    await start_quiz_for_user(callback.message, callback.from_user.id, "variables")
    await callback.answer()


@router.callback_query(F.data.startswith("start_quiz:"))
async def start_quiz_from_lesson(callback: CallbackQuery):
    lesson_key = callback.data.split(":", 1)[1]
    await start_quiz_for_user(callback.message, callback.from_user.id, lesson_key)
    await callback.answer()


@router.callback_query(F.data.startswith("quiz_answer:"))
async def handle_quiz_answer(callback: CallbackQuery):
    await callback.answer()

    try:
        _, lesson_key, question_index_raw, answer_index_raw = callback.data.split(":")
        question_index = int(question_index_raw)
        answer_index = int(answer_index_raw)
    except ValueError:
        await callback.message.answer("❌ Ошибка квиза. Запусти Quiz заново.")
        return

    if lesson_key not in QUIZZES:
        await callback.message.answer("❌ Такой квиз не найден.")
        return

    questions = QUIZZES[lesson_key]

    if question_index >= len(questions):
        await callback.message.answer("❌ Вопрос не найден. Запусти Quiz заново.")
        return

    state = user_quiz_state.setdefault(
        callback.from_user.id,
        {
            "lesson": lesson_key,
            "question_index": question_index,
            "correct_answers": 0,
            "answered": set(),
        },
    )

    answered = state.get("answered")
    if answered is None:
        answered = set()
        state["answered"] = answered

    question = questions[question_index]

    # Защита от повторного начисления XP при повторном клике на тот же старый вопрос.
    already_answered = question_index in answered

    if answer_index == question["correct"]:
        if not already_answered:
            user = await add_xp(callback.from_user.id, 2)
            state["correct_answers"] = int(state.get("correct_answers", 0)) + 1
            answered.add(question_index)

            await callback.message.answer(
                "✅ <b>Верно!</b>\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "⭐ +2 XP\n"
                f"📈 Всего XP: <b>{user.xp}</b>\n"
                f"🏆 Уровень: <b>{user.level}</b>",
                parse_mode="HTML",
            )
        else:
            await callback.message.answer("✅ Этот вопрос уже засчитан.")
    else:
        correct_text = question["a"][question["correct"]]
        await callback.message.answer(
            "❌ <b>Неверно</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"Правильный ответ: <b>{correct_text}</b>",
            parse_mode="HTML",
        )
        answered.add(question_index)

    next_index = question_index + 1

    if next_index < len(questions):
        state["question_index"] = next_index
        await send_quiz_question(callback.message, lesson_key, next_index)
        return

    correct_count = int(state.get("correct_answers", 0))
    total = len(questions)
    percent = int((correct_count / total) * 100) if total else 0

    await callback.message.answer(
        "🎉 <b>КВИЗ ЗАВЕРШЁН</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 Результат: <b>{correct_count} / {total}</b>\n"
        f"📈 Точность: <b>{percent}%</b>\n\n"
        "🚀 Можешь продолжать обучение!",
        parse_mode="HTML",
    )

    user_quiz_state.pop(callback.from_user.id, None)
