from datetime import datetime

from employee.models import Employee


def insert_employee(session, full_name, birth_date, gender):
    employee = Employee(full_name=full_name, birth_date=datetime.strptime(birth_date, "%Y-%m-%d"), gender=gender)
    session.add(employee)
    session.commit()
    print(f"Сотрудник {full_name} добавлен в базу данных")
