# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него
import time
import random


class TestManager:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print("Общее время исполнения кода составляет:", end_time - self.start_time, 'секунд')

with TestManager():
    time.sleep(random.randint(1, 3))
    print('Hello')