import time

class ContextManager:

    def __init__(self, t):
        self.t = t
        print('Менеджер контекстов создан')

    def __enter__(self):
        print('Начало работы с менеджером контекстов')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Конец работы с менеджером контекстов')
        print(f'Время работы менеджера контекстов: {time.time() - self.t}')

with ContextManager( t = time.time()):
    print('Работа с менеджером контекстов')
    input('Отчет по работе: ')
