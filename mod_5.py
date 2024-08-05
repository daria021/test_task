import time

from sqlalchemy import select
from sqlalchemy.orm import Session

from employee.models import Employee


def get_males(session: Session):
    employees = select(Employee).where(Employee.gender == "Male" and Employee.full_name.startswith("F"))

    start = time.time()

    objs = session.execute(employees)
    employees = objs.scalars().all()

    finish = time.time()

    res = finish - start
    res_msec = res * 1000
    print('Результат: ')
    for employee in employees:
        print(
            f"ФИО: {employee.full_name}, Дата рождения: {employee.birth_date}, Пол: {employee.gender}, Возраст: {employee.age} лет")
    print('Время работы в миллисекундах: ', res_msec,
          'Время работы в секундах: ', res)