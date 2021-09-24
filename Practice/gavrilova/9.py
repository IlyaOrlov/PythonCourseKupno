class User:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def setName(self):
        pass

    def getName(self, name):
        pass

    def setAge(self):
        pass

    def getAge(self, name):
        pass

class Worker(User):
    def __init__(self, name, age, salary):
        super(Worker, self).__init__(name, age)
        self.salary = salary

    def setSalary(self):
        pass

    def getSalary(self, name):
        pass

w1 = Worker("John", 25, 1000)
print(w1.salary)
w2 = Worker("Jack", 26, 2000)
print(w2.salary)
print (w1.salary+w2.salary)