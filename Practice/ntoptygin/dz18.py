# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него
import time

with open('text.txt', 'w') as f:
    start_time = time.time()
    f.write(input('Введите текст '))
    end_time = time.time()


print(end_time - start_time)
