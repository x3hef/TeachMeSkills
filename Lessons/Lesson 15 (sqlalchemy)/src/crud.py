from typing import Self

from sqlalchemy import select, update
from sqlalchemy.orm import Session


class CRUDManager:

    @classmethod
    def get_by_id(cls, session: Session, id_: int) -> Self:
        data = session.get_one(cls, id_)
        return data

    @classmethod
    def filter(cls, session: Session, **fields) -> list[Self]:
        query = select(cls)

        for field, value in fields.items():
            query = query.where(getattr(cls, field) == value)

        result = session.execute(query).scalars()
        return list(result)

    @classmethod
    def add(cls, session: Session, obj) -> Self:
        session.add(obj)

    def update(self, session: Session, values: list[str]) -> Self:
        query = update(self.__class__).values(
            **{v: getattr(self, v) for v in values}
        )
        session.execute(query)
        return self

    def delete(self, session: Session) -> None:
        session.delete(self)
