import json

from aiogram import Router, F
from aiogram.types import Message

from database.requests import add_xp

router = Router()


@router.message(F.web_app_data)
async def handle_web_app_data(message: Message):
    try:
        data = json.loads(message.web_app_data.data)
    except json.JSONDecodeError:
        await message.answer("❌ Не получилось прочитать результат игры.")
        return

    action = data.get("action")

    if action != "python_platformer_finish":
        await message.answer("🚀 Mini App отправил данные, но действие неизвестно.")
        return

    coins = int(data.get("coins", 0))
    score = int(data.get("score", 0))
    completed = bool(data.get("completed", False))

    xp = coins * 5

    if completed:
        xp += 25

    if xp > 150:
        xp = 150

    user = await add_xp(message.from_user.id, xp)

    text = (
        "🎮 <b>PYRUNNER RESULT</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🪙 Монеты: <b>{coins}</b>\n"
        f"⭐ Очки: <b>{score}</b>\n"
        f"🏁 Уровень пройден: <b>{'Да' if completed else 'Нет'}</b>\n\n"
        f"🎁 XP за игру: <b>+{xp}</b>"
    )

    if user:
        text += (
            "\n\n"
            f"📈 Всего XP: <b>{user.xp}</b>\n"
            f"🏆 Уровень: <b>{user.level}</b>"
        )

    await message.answer(
        text,
        parse_mode="HTML",
    )
