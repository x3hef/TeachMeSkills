from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.user import UserOut


class EventOut(BaseModel):
    id: int
    name: str
    meeting_time: datetime
    description: str
    users: list[UserOut]

    model_config = ConfigDict(from_attributes=True)
