import random

number_attempts = 0

a = int(input('Введите нижнюю границу диапазона: '))
b = int(input('Введите верхнюю границу диапазона: '))
number = random.randint(a, b)
print(f'Отлично, я загадал число между {a} и {b}. Сможешь угадать?')
x = 0

while True:
    x = input('Введи число: ')
    number_attempts += 1

    if not x.isnumeric():
        print('Извините, но вы ввели не число!')
        break

    x = int(x)

    if (x < a) or (x > b):
        print('Вы вышли за значения диапазона!')
        break

    elif x < number:
        print('Твое число меньше того, что я загадал.')

    elif x > number:
        print('Твое число больше загаданного мной.')

    else:
        x == number
        print(f'Ух ты! Ты угадал мое число, использовав {number_attempts} попыток!')
        break