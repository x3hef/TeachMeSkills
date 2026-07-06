import secrets
from datetime import datetime, timezone

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from .auth import get_admin_user, get_current_user, get_db, hash_password
from .database import Base, engine
from .models import Event, User
from .schemas import EventCreate, EventOut, RegisterOut, UserCreate, UserOut

app = FastAPI(title="Events API")

Base.metadata.create_all(bind=engine)


def current_time() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


def normalize_time(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value
    return value.astimezone(timezone.utc).replace(tzinfo=None)


@app.post("/api/users", response_model=RegisterOut, status_code=status.HTTP_201_CREATED)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    username_exists = db.scalar(select(User).where(User.username == data.username))
    if username_exists:
        raise HTTPException(status_code=400, detail="Username уже занят")

    email_exists = db.scalar(select(User).where(User.email == str(data.email)))
    if email_exists:
        raise HTTPException(status_code=400, detail="Email уже занят")

    first_user = db.scalar(select(User.id).limit(1)) is None
    token = secrets.token_urlsafe(32)

    user = User(
        username=data.username,
        email=str(data.email),
        password_hash=hash_password(data.password),
        api_token=token,
        is_admin=first_user,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "token": token,
        "is_admin": user.is_admin,
    }


@app.get("/api/users", response_model=list[UserOut])
def get_users(
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user),
):
    return db.scalars(select(User).order_by(User.id)).all()


@app.get("/api/events", response_model=list[EventOut])
def get_events(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    query = (
        select(Event)
        .options(selectinload(Event.users))
        .where(Event.meeting_time > current_time())
        .order_by(Event.meeting_time)
    )
    return db.scalars(query).all()


@app.post("/api/events", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def create_event(
    data: EventCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_admin_user),
):
    meeting_time = normalize_time(data.meeting_time)

    if meeting_time <= current_time():
        raise HTTPException(status_code=400, detail="Событие должно быть в будущем")

    event = Event(
        name=data.name,
        meeting_time=meeting_time,
        description=data.description,
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


@app.post("/api/event/{event_id}", response_model=EventOut)
def subscribe_to_event(
    event_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    query = select(Event).options(selectinload(Event.users)).where(Event.id == event_id)
    event = db.scalar(query)

    if event is None:
        raise HTTPException(status_code=404, detail="Событие не найдено")

    if event.meeting_time <= current_time():
        raise HTTPException(status_code=400, detail="Событие уже началось")

    if user not in event.users:
        event.users.append(user)
        db.commit()
        db.refresh(event)

    return event


@app.get("/api/events/my", response_model=list[EventOut])
def get_my_events(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    query = (
        select(Event)
        .options(selectinload(Event.users))
        .where(Event.users.any(User.id == user.id))
        .where(Event.meeting_time > current_time())
        .order_by(Event.meeting_time)
    )
    return db.scalars(query).all()
