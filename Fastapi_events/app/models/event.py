from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.association import subscriptions

if TYPE_CHECKING:
    from app.models.user import User


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    meeting_time: Mapped[datetime] = mapped_column(
        DateTime,
        index=True,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)

    users: Mapped[list[User]] = relationship(
        secondary=subscriptions,
        back_populates="events",
        lazy="selectin",
    )
