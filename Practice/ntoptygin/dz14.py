# Написать класс Pupil, у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд
# (c помощью метода sleep библиотеки time и randint библиотеки random)

import time
import random

class Man:

    def __init__(self, name):
        self.name = name
    def solve_task(self):
        print(f"I'm {self.name} and i'm not ready yet.")


class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()

a = Man('Andrey')
a.solve_task()

p = Pupil('Petr')
p.solve_task()



