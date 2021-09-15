# Написать класс Pupil, у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд
# (c помощью метода sleep библиотеки time и randint библиотеки random)

import time
import random

class Pupil:

    def __init__(self, name):
        self.name = name
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print(f"I'm {self.name} and i'm not ready yet")

a = Pupil('Petr')
a.solve_task()


