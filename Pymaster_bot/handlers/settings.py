from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from handlers.ai_assistant import clear_ai_history

router = Router()


def settings_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🤖 AI помощник",
                    callback_data="settings_ai",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🧹 Очистить AI память",
                    callback_data="settings_clear_ai",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ℹ️ О боте",
                    callback_data="settings_about",
                )
            ],
        ]
    )


@router.message(F.text == "⚙️ Настройки")
async def open_settings(message: Message):
    await message.answer(
        "⚙️ <b>НАСТРОЙКИ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Здесь можно управлять функциями бота.\n\n"
        "🤖 AI помощник — отвечает на вопросы по Python.\n"
        "🧹 Очистить AI память — сбрасывает историю диалога.",
        parse_mode="HTML",
        reply_markup=settings_keyboard(),
    )


@router.callback_query(F.data == "settings_ai")
async def settings_ai(callback: CallbackQuery):
    await callback.message.answer(
        "🤖 <b>AI ПОМОЩНИК</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Чтобы включить AI-помощника, нажми кнопку в меню:\n\n"
        "<b>🤖 AI Помощник</b>\n\n"
        "После этого можно писать вопросы по Python обычным сообщением.",
        parse_mode="HTML",
    )

    await callback.answer()


@router.callback_query(F.data == "settings_clear_ai")
async def settings_clear_ai(callback: CallbackQuery):
    clear_ai_history(callback.from_user.id)

    await callback.message.answer(
        "🧹 AI-память очищена.\n\n"
        "История твоего диалога с помощником сброшена."
    )

    await callback.answer()


@router.callback_query(F.data == "settings_about")
async def settings_about(callback: CallbackQuery):
    await callback.message.answer(
        "🐍 <b>PyMaster Bot</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Бот для изучения Python.\n\n"
        "Есть уроки, практика, quiz, прогресс, змейка, PyRunner и AI-помощник.",
        parse_mode="HTML",
    )

    await callback.answer()
