import os
import html
import asyncio

from dotenv import load_dotenv
from google import genai
from google.genai import types

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

router = Router()

active_ai_users = set()
ai_histories = {}

SYSTEM_PROMPT = """
Ты AI-помощник внутри Telegram-бота PyMaster Bot.

Твоя задача:
- помогать пользователю изучать Python;
- отвечать на русском языке;
- объяснять простыми словами;
- не писать слишком длинные ответы;
- если пользователь просит код — давать понятный код;
- если пользователь ошибся — мягко исправлять;
- быть дружелюбным наставником по Python.

Формат ответа:
- коротко;
- понятно;
- с примерами;
- без лишней воды.
"""


def get_ai_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🧹 Очистить диалог",
                    callback_data="ai_clear",
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ Выйти из AI",
                    callback_data="ai_exit",
                )
            ],
        ]
    )


def escape(value):
    return html.escape(str(value), quote=False)


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    return genai.Client(api_key=api_key)


def clear_ai_history(user_id: int):
    ai_histories.pop(user_id, None)


def add_to_history(user_id: int, role: str, content: str):
    if user_id not in ai_histories:
        ai_histories[user_id] = []

    ai_histories[user_id].append(
        {
            "role": role,
            "content": content,
        }
    )

    if len(ai_histories[user_id]) > 8:
        ai_histories[user_id] = ai_histories[user_id][-8:]


def build_prompt(user_id: int, user_message: str):
    history = ai_histories.get(user_id, [])

    history_text = ""

    for item in history:
        role = item["role"]
        content = item["content"]

        if role == "user":
            history_text += f"Пользователь: {content}\n"
        else:
            history_text += f"AI: {content}\n"

    return (
        "История диалога:\n"
        f"{history_text}\n\n"
        "Новое сообщение пользователя:\n"
        f"{user_message}\n\n"
        "Ответь как наставник по Python:"
    )


@router.message(F.text == "🤖 AI Помощник")
async def open_ai_assistant(message: Message):
    active_ai_users.add(message.from_user.id)

    await message.answer(
        "🤖 <b>AI ПОМОЩНИК PYMASTER</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Теперь можешь писать вопросы по Python.\n\n"
        "Например:\n"
        "• Что такое переменная?\n"
        "• Объясни цикл for\n"
        "• Почему мой код не работает?\n"
        "• Дай задачу по спискам\n\n"
        "Чтобы выйти — нажми кнопку ниже.",
        parse_mode="HTML",
        reply_markup=get_ai_keyboard(),
    )


@router.message(lambda message: message.from_user and message.from_user.id in active_ai_users)
async def handle_ai_message(message: Message):
    user_id = message.from_user.id

    if not message.text:
        await message.answer("Пока я умею отвечать только на текстовые сообщения.")
        return

    menu_buttons = [
        "📚 Учиться",
        "🧠 Quiz",
        "🐍 Змейка",
        "🕹️ PyRunner",
        "🏆 Прогресс",
        "⚙️ Настройки",
    ]

    if message.text in menu_buttons:
        active_ai_users.discard(user_id)

        await message.answer(
            "🤖 AI-режим выключен.\n\n"
            "Теперь кнопки меню снова работают обычно."
        )
        return

    client = get_gemini_client()

    if client is None:
        await message.answer(
            "❌ <b>GEMINI_API_KEY не найден</b>\n\n"
            "Добавь в файл <code>.env</code>:\n\n"
            "<code>GEMINI_API_KEY=твой_ключ</code>\n"
            "<code>GEMINI_MODEL=gemini-2.5-flash</code>\n\n"
            "Потом перезапусти бота.",
            parse_mode="HTML",
        )
        return

    thinking_message = await message.answer("🤖 Думаю...")

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    try:
        prompt = build_prompt(user_id, message.text)

        response = await asyncio.to_thread(
            client.models.generate_content,
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                max_output_tokens=700,
                temperature=0.7,
            ),
        )

        answer = getattr(response, "text", None)

        if not answer:
            answer = "Я получил пустой ответ от модели. Попробуй переформулировать вопрос."

        answer = answer.strip()

        if len(answer) > 3500:
            answer = answer[:3500] + "\n\n...ответ был сокращён."

        add_to_history(user_id, "user", message.text)
        add_to_history(user_id, "assistant", answer)

        try:
            await thinking_message.delete()
        except Exception:
            pass

        await message.answer(
            escape(answer),
            parse_mode="HTML",
            reply_markup=get_ai_keyboard(),
        )

    except Exception as error:
        try:
            await thinking_message.delete()
        except Exception:
            pass

        error_text = f"{type(error).__name__}: {error}"

        print("GEMINI ERROR:", error_text)

        await message.answer(
            "❌ <b>Ошибка Gemini AI</b>\n\n"
            f"<code>{escape(error_text)}</code>\n\n"
            "Что проверить:\n"
            "1. Установлено: <code>uv add google-genai</code>\n"
            "2. В .env есть <code>GEMINI_API_KEY</code>\n"
            "3. В .env есть <code>GEMINI_MODEL=gemini-2.5-flash</code>\n"
            "4. Ты перезапустил бота после изменения .env",
            parse_mode="HTML",
        )


@router.callback_query(F.data == "ai_clear")
async def clear_ai(callback: CallbackQuery):
    clear_ai_history(callback.from_user.id)

    await callback.message.answer(
        "🧹 История AI-диалога очищена.\n\n"
        "Можешь задать новый вопрос."
    )

    await callback.answer()


@router.callback_query(F.data == "ai_exit")
async def exit_ai(callback: CallbackQuery):
    active_ai_users.discard(callback.from_user.id)

    await callback.message.answer(
        "❌ AI-помощник выключен.\n\n"
        "Можешь продолжать обучение 📚"
    )

    await callback.answer()
