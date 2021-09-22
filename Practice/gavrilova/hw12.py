import time
import random

class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()

m = Man('Marya')
print(f'Are you ready {m.name}?')
m.solve_task()

p = Pupil('Evgeniy')
print(f'And you {p.name}?')
p.solve_task()