from employee.models import Employee


def display_employees(session):
    employees = session.query(Employee).order_by(Employee.full_name).all()
    for employee in employees:
        print(
            f"ФИО: {employee.full_name}, Дата рождения: {employee.birth_date}, Пол: {employee.gender}, Возраст: {employee.age} лет")
