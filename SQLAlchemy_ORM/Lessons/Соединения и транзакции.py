from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///:memory:', echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select 'Hello world'"))
    print(result.all()) # - вывод всех данных
    print(result.scalar_one())
    print(result.scalar_one_or_none())

# 2026-04-18 12:25:19,851 INFO sqlalchemy.engine.Engine BEGIN (implicit) - начало транзакции
# 2026-04-18 12:25:19,851 INFO sqlalchemy.engine.Engine select 'Hello world'
# 2026-04-18 12:25:19,851 INFO sqlalchemy.engine.Engine [generated in 0.00022s] ()
# [('Hello world',)]
# 2026-04-18 12:25:19,851 INFO sqlalchemy.engine.Engine ROLLBACK - конец транзакции

