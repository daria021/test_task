from datetime import datetime

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Employee(Base):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[int] = Column(String(100), nullable=False)
    birth_date: Mapped[datetime] = Column(Date, nullable=False)
    gender: Mapped[str] = Column(String(10), nullable=False)

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
