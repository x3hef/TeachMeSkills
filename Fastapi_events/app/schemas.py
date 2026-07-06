from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=4, max_length=100)


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class RegisterOut(UserOut):
    token: str
    is_admin: bool


class EventCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    meeting_time: datetime
    description: str = Field(min_length=2)


class EventOut(BaseModel):
    id: int
    name: str
    meeting_time: datetime
    description: str
    users: list[UserOut]

    model_config = ConfigDict(from_attributes=True)
