from sqlalchemy import Column, ForeignKey, Integer, Table

from app.db.base import Base

subscriptions = Table(
    "subscriptions",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
)
