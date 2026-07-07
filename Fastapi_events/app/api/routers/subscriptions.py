from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import CurrentUser, DatabaseSession
from app.schemas import EventOut
from app.services import events as event_service

router = APIRouter(prefix="/api/event", tags=["events"])


@router.post("/{event_id}", response_model=EventOut)
async def subscribe_to_event(
    event_id: int,
    db: DatabaseSession,
    user: CurrentUser,
) -> EventOut:
    try:
        event = await event_service.subscribe(db, event_id, user)
    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return EventOut.model_validate(event)
