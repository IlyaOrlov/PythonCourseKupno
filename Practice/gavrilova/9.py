class User:

    name = ' '
    age = 0
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class Worker(User):

    salary = 0
#    def __init__(self, name, age, salary):
#        super(Worker, self).__init__(name, age)
#        self.salary = salary

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


w1 = Worker()
w1.setName('John')
print(w1.getName())
w1.setAge(25)
print(w1.getAge())
w1.setSalary(1000)
print(w1.getSalary())
w2 = Worker()
w2.setName('Jack')
print(w2.getName())
w2.setAge(26)
print(w2.getAge())
w2.setSalary(2000)
print(w2.getSalary())
s = w1.getSalary() + w2.getSalary()
print(f'Сумма зарплат объектов John и Jack {s} ')
#w1 = Worker("John", 25, 1000)
#print(w1.salary)
#w2 = Worker("Jack", 26, 2000)
#print(w2.salary)
#print (w1.salary+w2.salary)