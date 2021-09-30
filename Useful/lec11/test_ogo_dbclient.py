from ogo_dbclient import DBClient
import os


db_type = "sqlite"
db_name = "ogo.db"
db_exists = os.path.exists(db_name)

if not db_exists:
    with DBClient(db_type, db_name) as dbc:
        dbc.create_schema()

        dbc.insert_position("инженер", 50000)
        dbc.insert_position("старший инженер", 51000)
        dbc.insert_position("менеджер проекта", 100000)

        pid = dbc.insert_project("Важный")
        eid = dbc.insert_employee("Иванов И.И.", "инженер", 30000,
                                  "ivanovi", "ivanov123")
        dbc.add_employee_to_project(eid, pid)

        eid = dbc.insert_employee("Петров П.П.", "старший инженер", 50000,
                                  "petrovp", "p1e2t3")
        dbc.add_employee_to_project(eid, pid)

        pid = dbc.insert_project("Срочный")
        dbc.add_employee_to_project(eid, pid)

        eid = dbc.insert_employee("Сидоров С.С.", "менеджер проекта", 30000,
                            "sidorovs", "zayka88")
        dbc.add_employee_to_project(eid, pid)



login = input("Логин: ")
pwd = input("Пароль: ")
with DBClient(db_type, db_name) as dbc:
    #dbc.show_all()
    res = dbc.authentication(login, pwd)
    if res:
        user = res._asdict()
        print("Здравствуйте, {}".format(user['name']))
        if user['position'] == "менеджер проекта":
            dbc.show_manager_info(user['project_id'])

            id_upd = int(input("Изменение премии. ID сотрудника (0 - отмена): "))
            if id_upd:
                if (id_upd != user['id'] and
                        dbc.is_employee_in_project(id_upd, user['project_id'])):
                    new_bonus = input("Новая премия: ")
                    dbc.update_employee_bonus(id_upd, new_bonus)
                    print("Результат:")
                    dbc.show_manager_info(user['project_id'])
                else:
                    print("Невозможно изменить премию для данного сотрудника")

            id_del = int(input("Удаление сотрудника. ID сотрудника (0 - отмена): "))
            if id_del:
                if id_del != user['id']:
                    dbc.delete_employee_from_project(id_del, user['project_id'])
                    print("Результат:")
                    dbc.show_manager_info(user['project_id'])
                else:
                    print("Невозможно удалить данного сотрудника из проекта")
        else:
            dbc.show_employee_info(user['id'])
    else:
        print("Доступ запрещен")

