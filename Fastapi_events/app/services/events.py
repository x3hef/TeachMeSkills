from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import Event, User
from app.time_utils import current_time


def event_query():
    return select(Event).options(selectinload(Event.users))


async def get_upcoming_events(db: AsyncSession) -> list[Event]:
    query = (
        event_query()
        .where(Event.meeting_time > current_time())
        .order_by(Event.meeting_time)
    )
    result = await db.scalars(query)
    return list(result.unique().all())


async def subscribe(db: AsyncSession, event_id: int, user: User) -> Event:
    event = await db.scalar(event_query().where(Event.id == event_id))
    if event is None:
        raise LookupError("Событие не найдено")
    if event.meeting_time <= current_time():
        raise ValueError("Событие уже началось")

    if all(subscriber.id != user.id for subscriber in event.users):
        event.users.append(user)
        await db.commit()

    return event


async def get_user_events(db: AsyncSession, user: User) -> list[Event]:
    query = (
        event_query()
        .where(Event.users.any(User.id == user.id))
        .order_by(Event.meeting_time)
    )
    result = await db.scalars(query)
    return list(result.unique().all())
