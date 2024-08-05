from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import config

DATABASE_URL = config.db

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine, class_=Session, expire_on_commit=False)


class Base(DeclarativeBase):
    __abstract__ = True


@contextmanager
def get_session() -> Generator[Session, None, None]:
    session = session_maker()
    try:
        yield session
    finally:
        session.close()
