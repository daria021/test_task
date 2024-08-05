import time
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_

from employee.models import Employee


def optimized_get_males(session: Session):
    query = select(Employee).where(and_(
        Employee.gender == "Male",
        Employee.full_name.like("F%")))

    start = time.time()

    result = session.execute(query)
    result.scalars().all()

    finish = time.time()

    res = finish - start
    res_msec = res * 1000
    print('Время работы в миллисекундах: ', res_msec,
          'Время работы в секундах: ', res)


def optimized_get_males_2(session: Session):
    start = time.time()

    result = session.execute(text("""SELECT * FROM public.employees WHERE gender = 'Male' AND full_name LIKE 'F%';"""))
    result.fetchall()

    finish = time.time()

    res = finish - start
    res_msec = res * 1000
    print('Время работы в миллисекундах: ', res_msec,
          'Время работы в секундах: ', res)
