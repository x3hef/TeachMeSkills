from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import FSInputFile
from database.requests import get_user

router = Router()


@router.message(F.text == "🏆 Прогресс")
async def profile(message: Message):
    photo = FSInputFile("media/profile.png")
    user = await get_user(message.from_user.id)

    if user is None:
        await message.answer("Сначала нажми /start")
        return

    xp_to_next_level = user.level * 100
    progress = int((user.xp / xp_to_next_level) * 10)

    progress_bar = "🟨" * progress + "⬛" * (10 - progress)

    await message.answer_photo(
        photo=photo,
        caption=(
            "🏆 <b>ТВОЙ ПРОГРЕСС</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"

            f"👤 <b>{user.first_name}</b>\n\n"

            f"⭐ XP: <b>{user.xp}</b> / {xp_to_next_level}\n"
            f"📈 Уровень: <b>{user.level}</b>\n\n"

            f"{progress_bar}\n\n"

            "🚀 Продолжай обучение,\n"
            "чтобы открыть новые уроки!"
        ),
        parse_mode="HTML",
    )
