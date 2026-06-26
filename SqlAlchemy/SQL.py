
# Подключение к БД
#####################################################
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db") # - путь к базе
# engine - мост к базе данных
#####################################################
# Base — основа всех таблиц
#####################################################
from sqlalchemy.orm import declarative_base

Base = declarative_base()
#####################################################
# Создание таблицы (Model)
#####################################################
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Создание таблицы в базе
Base.metadata.create_all(engine)

# Session — сердце работы с данными

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Добавление данных

user = User(name="Анна", age=22)

session.add(user)
session.commit()

# Получение данных
users = session.query(User).all()

for user in users:
    print(user.name, user.age)

# Фильтрация
users = session.query(User).filter(User.age > 18).all()

# Обновление данных

user = session.query(User).first()
user.age = 30

session.commit()

# Удаление
user = session.query(User).first()

session.delete(user)
session.commit()

print(session.query(User).all())