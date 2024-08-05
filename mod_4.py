import factory
from factory.fuzzy import FuzzyChoice
from faker import Faker
from sqlalchemy.orm import Session

from employee.models import Employee

fake = Faker()


class EmployeeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Employee
        sqlalchemy_session_persistence = 'commit'

    full_name = factory.LazyAttribute(lambda x: fake.name())
    birth_date = factory.LazyAttribute(lambda x: fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=65))
    gender = FuzzyChoice(choices=['Male', 'Female'])

    @classmethod
    def create_special_batch(cls, session, count):
        special_employees = cls.create_batch(gender='Male', size=count)
        for emp in special_employees:
            last_name = fake.last_name_male()
            first_names = fake.first_name_male() + " " + fake.first_name_male()
            emp.full_name = f"F{last_name} {first_names}"
            session.add(emp)
        session.commit()
        return special_employees

    @classmethod
    def set_session(cls, session):
        cls._meta.sqlalchemy_session = session


def generate_employees(session: Session, count: int = 1000000, special_count: int = 100):
    EmployeeFactory.set_session(session)
    employees = EmployeeFactory.create_batch(size=count)
    special_employees = EmployeeFactory.create_special_batch(session=session, count=special_count)
    session.add_all(employees + special_employees)
    session.commit()
    print(f"{count + special_count} сотрудников добавлено в базу данных")
