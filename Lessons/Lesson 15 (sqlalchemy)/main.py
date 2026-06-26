from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import Base, User, Product
from src.db_connector import engine, session_maker_class


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_test_users(session: Session):
    user = User(
        username='admin',
        email='admin@gmail.com',
        password='435070923c47890t',
        first_name='John',
        last_name='Doe',
    )
    user2 = User(
        username="igor",
        email="igor@gmail.com",
        password="745897648597",
        first_name="Igor",
        last_name="Ivanovich",
    )

    session.add_all([user, user2])


def create_test_products(session: Session):
    session.add_all(
        [
            Product(name="apple", price=20),
            Product(name="banana", price=30),
            Product(name="orange", price=40),
            Product(name="mango", price=50),
            Product(name="strawberry", price=60),
            Product(name="peach", price=70),
            Product(name="grape", price=80),
        ]
    )


def find_products(session: Session):
    pass


if __name__ == '__main__':
    create_tables()

    with session_maker_class() as session:
        create_test_users(session)
        create_test_products(session)
        session.commit()

        query = select(User).where(User.username == 'admin')
        res = session.execute(query).scalar_one()

        user = User.get_by_id(session, 1)

        Product.get_by_id()

        print(user.email)

        user.email = 'admin2@gmail.com'

        user.update(session, ["email"])