from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models import User

security = HTTPBearer(auto_error=False)

DatabaseSession = Annotated[AsyncSession, Depends(get_db)]
Credentials = Annotated[
    HTTPAuthorizationCredentials | None,
    Depends(security),
]


async def get_current_user(
    credentials: Credentials,
    db: DatabaseSession,
) -> User:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Требуется API токен",
        )

    user = await db.scalar(
        select(User).where(User.api_token == credentials.credentials)
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный API токен",
        )

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


async def get_admin_user(user: CurrentUser) -> User:
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Доступ только для администратора",
        )
    return user


AdminUser = Annotated[User, Depends(get_admin_user)]
