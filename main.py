import sys

from db import engine, get_session
from mod_1 import create_table
from mod_2 import insert_employee
from mod_3 import display_employees
from mod_4 import generate_employees
from mod_5 import get_males
from mod_6 import optimized_get_males, optimized_get_males_2


def main():
    if len(sys.argv) < 2:
        print("Необходимо указать режим работы приложения")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == '1':
        create_table(engine)
    elif mode == '2':
        if len(sys.argv) != 5:
            print("Необходимо указать ФИО, дату рождения и пол")
            sys.exit(1)
        full_name = sys.argv[2]
        birth_date = sys.argv[3]
        gender = sys.argv[4]
        with get_session() as session:
            insert_employee(session, full_name, birth_date, gender)
    elif mode == '3':
        with get_session() as session:
            display_employees(session)
    elif mode == '4':
        with get_session() as session:
            generate_employees(session)
    elif mode == '5':
        with get_session() as session:
            get_males(session)
    elif mode == '6':
        with get_session() as session:
            optimized_get_males(session)
            optimized_get_males_2(session)
    else:
        print("Неизвестный режим работы")


if __name__ == "__main__":
    main()
