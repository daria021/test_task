from db import Base


def create_table(engine):
    Base.metadata.create_all(engine)
    print("Таблица employees создана")
