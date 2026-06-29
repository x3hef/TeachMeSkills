from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from keyboards.main_menu import main_menu
from database.requests import add_user, get_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user = await get_user(message.from_user.id)

    if user is None:
        await add_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
        )

    photo = FSInputFile("media/avatar.png")

    await message.answer_photo(
        photo=photo,
        caption=(
            "⚡ <b>PYMASTER BOT</b>\n"
            "<blockquote>Учись. Практикуйся. Развивайся.</blockquote>\n\n"
            "📖 <b>Уроки по Python</b>\n"
            "🧠 <b>Интерактивные Quiz</b>\n"
            "🏆 <b>XP • Уровни • Достижения</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "👇 <b>Выбери раздел ниже</b>"
        ),
        parse_mode="HTML",
        reply_markup=main_menu,
    )


@router.message(F.text == "⚙️ Настройки")
async def settings(message: Message):
    await message.answer(
        "⚙️ <b>НАСТРОЙКИ</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Пока здесь будут настройки профиля, уведомлений и темы.\n\n"
        "Скоро добавим новые возможности 🔧",
        parse_mode="HTML",
    )
