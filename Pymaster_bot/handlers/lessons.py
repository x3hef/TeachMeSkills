import html

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from handlers.states import PracticeState
from database.requests import add_xp, complete_lesson
from keyboards.dynamic_lesson_keyboard import get_lesson_keyboard
from content.lessons_data import LESSONS, LESSON_ORDER

router = Router()


def safe_text(value):
    """
    Защита HTML.
    Telegram ломается, если в тексте/коде есть < > &
    Например: while x < 5:
    """
    if value is None:
        return ""
    return html.escape(str(value), quote=False)


def get_next_lesson_key(current_key: str):
    if current_key not in LESSON_ORDER:
        return None

    current_index = LESSON_ORDER.index(current_key)
    next_index = current_index + 1

    if next_index >= len(LESSON_ORDER):
        return None

    return LESSON_ORDER[next_index]


def build_keyboard(lesson_key: str, lesson: dict):
    next_key = get_next_lesson_key(lesson_key)

    try:
        return get_lesson_keyboard(lesson_key, lesson, next_key)
    except TypeError:
        return get_lesson_keyboard(lesson_key, lesson)


async def send_lesson(message: Message, lesson_key: str):
    if lesson_key not in LESSONS:
        await message.answer("❌ Урок не найден")
        return

    lesson = LESSONS[lesson_key]

    title = safe_text(lesson.get("title", "Урок"))
    text = safe_text(lesson.get("text", ""))
    code = safe_text(lesson.get("code", ""))
    idea = safe_text(lesson.get("idea", ""))

    await message.answer(
        f"📘 <b>{title.upper()}</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"{text}\n\n"
        "<b>💻 Пример кода</b>\n"
        f"<pre><code>{code}</code></pre>\n\n"
        "<b>📌 Главное</b>\n"
        f"{idea}",
        parse_mode="HTML",
        reply_markup=build_keyboard(lesson_key, lesson),
    )


@router.message(F.text.lower() == "переменные")
async def start_variables(message: Message):
    await send_lesson(message, "variables")


@router.callback_query(F.data.startswith("lesson_"))
async def open_lesson(callback: CallbackQuery):
    await callback.answer()

    lesson_key = callback.data.replace("lesson_", "")

    if lesson_key not in LESSONS:
        await callback.message.answer("❌ Урок не найден")
        return

    await send_lesson(callback.message, lesson_key)


@router.callback_query(F.data.startswith("understood_"))
async def understood(callback: CallbackQuery):
    await callback.answer()

    lesson_key = callback.data.replace("understood_", "")

    if lesson_key not in LESSONS:
        await callback.message.answer("❌ Ошибка урока")
        return

    await complete_lesson(callback.from_user.id, lesson_key)

    user = await add_xp(callback.from_user.id, 5)

    if user:
        await callback.message.answer(
            "🎉 <b>УРОК ПРОЙДЕН</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Прогресс сохранён.\n\n"
            "⭐ <b>+5 XP</b>\n"
            f"📈 Всего XP: <b>{user.xp}</b>\n"
            f"🏆 Уровень: <b>{user.level}</b>",
            parse_mode="HTML",
        )
    else:
        await callback.message.answer(
            "🎉 <b>УРОК ПРОЙДЕН</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Прогресс сохранён.",
            parse_mode="HTML",
        )


@router.callback_query(F.data.startswith("practice_"))
async def practice(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    lesson_key = callback.data.replace("practice_", "")

    if lesson_key not in LESSONS:
        await callback.message.answer("❌ Практика пока недоступна")
        return

    lesson = LESSONS[lesson_key]
    title = safe_text(lesson.get("title", "Практика"))

    practice_data = lesson.get("practice", {})
    task = safe_text(
        practice_data.get(
            "task",
            "Практическое задание для этого урока скоро появится.",
        )
    )

    await state.update_data(lesson=lesson_key)

    await callback.message.answer(
        f"⭐ <b>ПРАКТИКА: {title}</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"{task}\n\n"
        "✍️ Отправь ответ сообщением",
        parse_mode="HTML",
    )

    await state.set_state(PracticeState.waiting_variables_answer)


@router.callback_query(F.data.startswith("next_"))
async def next_lesson(callback: CallbackQuery):
    await callback.answer()

    current_key = callback.data.replace("next_", "")
    next_key = get_next_lesson_key(current_key)

    if next_key is None:
        await callback.message.answer("🏁 Это последний урок")
        return

    await send_lesson(callback.message, next_key)


@router.callback_query(F.data == "back_lessons")
async def back_lessons(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer(
        "📚 <b>PYTHON ROADMAP</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Нажми <b>📚 Учиться</b>, чтобы открыть разделы.",
        parse_mode="HTML",
    )