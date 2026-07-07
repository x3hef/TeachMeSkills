from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.schemas import UserCreate
from app.security import generate_api_token, hash_password


async def create_user(db: AsyncSession, data: UserCreate) -> User:
    username_exists = await db.scalar(
        select(User.id).where(User.username == data.username)
    )
    if username_exists is not None:
        raise ValueError("Username уже занят")

    email = str(data.email).lower()
    email_exists = await db.scalar(select(User.id).where(User.email == email))
    if email_exists is not None:
        raise ValueError("Email уже занят")

    first_user = await db.scalar(select(User.id).limit(1)) is None
    user = User(
        username=data.username,
        email=email,
        password_hash=hash_password(data.password),
        api_token=generate_api_token(),
        is_admin=first_user,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_all_users(db: AsyncSession) -> list[User]:
    result = await db.scalars(select(User).order_by(User.id))
    return list(result.all())
