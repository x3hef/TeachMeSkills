from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from database.requests import get_completed_lessons, get_progress
from keyboards.learning_keyboard import (
    roadmap_keyboard,
    get_basics_keyboard,
    get_collections_keyboard,
    get_functions_keyboard,
    get_oop_keyboard,
)

router = Router()


@router.message(F.text == "📚 Учиться")
async def learning(message: Message):
    await message.answer(
        "📚 <b>PYTHON ROADMAP</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Выбери раздел обучения 👇",
        parse_mode="HTML",
        reply_markup=roadmap_keyboard,
    )


@router.callback_query(F.data == "section_basics")
async def section_basics(callback: CallbackQuery):
    completed = await get_completed_lessons(callback.from_user.id)

    await callback.message.answer(
        "🐍 <b>ОСНОВЫ PYTHON</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Пройдено\n"
        "⭐ Доступно\n\n"
        "Все темы открыты. Выбирай урок 👇",
        parse_mode="HTML",
        reply_markup=get_basics_keyboard(completed),
    )

    await callback.answer()


@router.callback_query(F.data == "section_collections")
async def section_collections(callback: CallbackQuery):
    completed = await get_completed_lessons(callback.from_user.id)

    await callback.message.answer(
        "📦 <b>КОЛЛЕКЦИИ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Пройдено\n"
        "⭐ Доступно\n\n"
        "Все темы открыты. Выбирай урок 👇",
        parse_mode="HTML",
        reply_markup=get_collections_keyboard(completed),
    )

    await callback.answer()


@router.callback_query(F.data == "section_functions")
async def section_functions(callback: CallbackQuery):
    completed = await get_completed_lessons(callback.from_user.id)

    await callback.message.answer(
        "⚙️ <b>ФУНКЦИИ И ФАЙЛЫ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Пройдено\n"
        "⭐ Доступно\n\n"
        "Все темы открыты. Выбирай урок 👇",
        parse_mode="HTML",
        reply_markup=get_functions_keyboard(completed),
    )

    await callback.answer()


@router.callback_query(F.data == "section_oop")
async def section_oop(callback: CallbackQuery):
    completed = await get_completed_lessons(callback.from_user.id)

    await callback.message.answer(
        "🏛️ <b>ООП</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✅ Пройдено\n"
        "⭐ Доступно\n\n"
        "Все темы открыты. Выбирай урок 👇",
        parse_mode="HTML",
        reply_markup=get_oop_keyboard(completed),
    )

    await callback.answer()


@router.callback_query(F.data == "progress")
async def progress(callback: CallbackQuery):
    data = await get_progress(callback.from_user.id)

    await callback.message.answer(
        "🏆 <b>ТВОЙ ПРОГРЕСС</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"📚 Уроки: <b>{data['done']} / {data['total']}</b>\n"
        f"📈 Прогресс: <b>{data['percent']}%</b>\n\n"
        f"{data['bar']}\n\n"
        "🚀 Продолжай обучение!",
        parse_mode="HTML",
    )

    await callback.answer()


@router.callback_query(F.data == "back_roadmap")
async def back_roadmap(callback: CallbackQuery):
    await callback.message.answer(
        "📚 <b>PYTHON ROADMAP</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Выбери раздел обучения 👇",
        parse_mode="HTML",
        reply_markup=roadmap_keyboard,
    )

    await callback.answer()
