from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine("mysql+mysqldb://root:password@localhost/general", echo=False)
# engine = create_engine("sqlite:///db.sqlite3")

session_maker_class = sessionmaker(bind=engine, autoflush=False, autocommit=False)