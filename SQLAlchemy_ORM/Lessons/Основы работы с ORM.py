# SQLAlchemy - это инструмент, который позволяет
# работать с базой данных через Python
# вместо SQL использовать обычный код

# Без SQLAlchemy
# SELECT * FROM users;
                     # - смысл один и тот же
# с SQLAlchemy
# session.query(User).all()

# Из чего состоит:

# Engine
    # - подключение к базе данных
    # - чтобы вообще иметь доступ к базе

# Как используется
    # engine = create_engine("sqlite:///db.db")
    # один раз создаёшь → дальше используешь

# Model(class)

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# Session - объект для работы с базой
# - читать
# - добавлять
# - удалять

# Как используется:
# session = Session() - Все делается через него

# Commit
# - сохранение изменения
# - без этого база не обновится

# Как используется:
# session.commit()
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///users.db')

# создаём таблицы
Base.metadata.create_all(engine)

# создаём сессию
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

pasha = User(name='pasha', age=20)
session.add(pasha)
session.commit()