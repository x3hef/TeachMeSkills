from sqlalchemy import create_engine, Integer, Column, String, func, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base() # базовый класс от которого будут наследоваться все классы
engine = create_engine('sqlite:///demo.db')
Session = sessionmaker(bind=engine)
session = Session()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer, default=0)

    videos = relationship("Videos", back_populates="user")

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    views = Column(Integer, default=0)

    creatoe_id = Column(Integer, ForeignKey('users.id')) # Внешний ключ

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)

# Base.metadata.create_all(engine) # создание бд
#
# maria = User(name='Maria', age=20)
# oleg = User(name='Oleg', age=21)
#
# session.add(maria)
# session.add(oleg)
# session.commit()

#users = session.query(User).all()
#for user in users:
#    print(user.name)

# Агрегатные функции

# users = session.query(func.max(User.id)).all()
# print(users)


