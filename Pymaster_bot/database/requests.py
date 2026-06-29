from sqlalchemy import select
from database.db import session_maker
from database.models import User, LessonProgress


async def get_user(telegram_id: int):
    async with session_maker() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()


async def add_user(telegram_id: int, username: str | None, first_name: str):
    async with session_maker() as session:
        user = await session.scalar(
            select(User).where(User.telegram_id == telegram_id)
        )

        if not user:
            user = User(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name,
                xp=0,
                level=1
            )
            session.add(user)

        await session.commit()


async def add_xp(telegram_id: int, xp_amount: int):
    async with session_maker() as session:
        user = await session.scalar(
            select(User).where(User.telegram_id == telegram_id)
        )

        if user:
            user.xp += xp_amount

            if user.xp >= user.level * 100:
                user.level += 1

            await session.commit()
            return user


async def complete_lesson(telegram_id: int, lesson_key: str):
    async with session_maker() as session:
        progress = await session.scalar(
            select(LessonProgress).where(
                LessonProgress.telegram_id == telegram_id,
                LessonProgress.lesson_key == lesson_key,
            )
        )

        if not progress:
            progress = LessonProgress(
                telegram_id=telegram_id,
                lesson_key=lesson_key,
                is_completed=1,
            )
            session.add(progress)
        else:
            progress.is_completed = 1

        await session.commit()


async def get_completed_lessons(telegram_id: int):
    async with session_maker() as session:
        result = await session.execute(
            select(LessonProgress.lesson_key).where(
                LessonProgress.telegram_id == telegram_id,
                LessonProgress.is_completed == 1,
            )
        )

        return set(result.scalars().all())


from content.lessons_data import LESSON_ORDER


async def get_progress(telegram_id: int):
    completed = await get_completed_lessons(telegram_id)

    total = len(LESSON_ORDER)
    done = len(completed)

    percent = int((done / total) * 100) if total > 0 else 0

    # визуальный бар (10 блоков)
    bars = int(percent / 10)
    bar_str = "🟩" * bars + "⬛" * (10 - bars)

    return {
        "done": done,
        "total": total,
        "percent": percent,
        "bar": bar_str,
    }
