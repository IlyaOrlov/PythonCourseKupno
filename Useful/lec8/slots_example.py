class Employee:
    __slots__ = ('name', 'surname', 'salary')

    def __init__(self):
        self.name = 'No name'
        self.surname = 'No surname'
        self.salary = 0

    def save_to_db(self):
        with open('mydb', 'w') as f:
            f.write(f'name = {self.name}')
            f.write(f'surname = {self.surname}')
            f.write(f'salary = {self.salary}')


emp = Employee()
emp.salary = int(input('input salary: '))
#emp.speed = 50
print(emp.salary)
