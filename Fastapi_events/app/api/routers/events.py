from fastapi import APIRouter

from app.api.dependencies import CurrentUser, DatabaseSession
from app.schemas import EventOut
from app.services import events as event_service

router = APIRouter(prefix="/api/events", tags=["events"])


@router.get("", response_model=list[EventOut])
async def get_events(
    db: DatabaseSession,
    _user: CurrentUser,
) -> list[EventOut]:
    events = await event_service.get_upcoming_events(db)
    return [EventOut.model_validate(event) for event in events]


@router.get("/my", response_model=list[EventOut])
async def get_my_events(
    db: DatabaseSession,
    user: CurrentUser,
) -> list[EventOut]:
    events = await event_service.get_user_events(db, user)
    return [EventOut.model_validate(event) for event in events]
