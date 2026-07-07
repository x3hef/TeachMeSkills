from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import AdminUser, DatabaseSession
from app.schemas import RegisterOut, UserCreate, UserOut
from app.services import users as user_service

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("", response_model=RegisterOut, status_code=status.HTTP_201_CREATED)
async def register_user(data: UserCreate, db: DatabaseSession) -> RegisterOut:
    try:
        user = await user_service.create_user(db, data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return RegisterOut(
        id=user.id,
        username=user.username,
        email=user.email,
        token=user.api_token,
    )


@router.get("", response_model=list[UserOut])
async def get_users(
    db: DatabaseSession,
    _admin: AdminUser,
) -> list[UserOut]:
    users = await user_service.get_all_users(db)
    return [UserOut.model_validate(user) for user in users]
