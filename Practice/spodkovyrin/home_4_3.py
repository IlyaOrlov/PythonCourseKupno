import random

number_attempts = 0

a = int(input('Введите нижнюю границу диапазона: '))
b = int(input('Введите верхнюю границу диапазона: '))
number = random.randint(a, b)
print('Отлично, я загадал число между {} и {}. Сможешь угадать?'.format(a, b))
x = 0

while True:
    x = input('Введи число: ')
    number_attempts += 1

    if not x.isnumeric():
        print('Извините, но вы ввели не число!')
        break

    if int(x) < number:
        print('Твое число меньше того, что я загадал.')

    if int(x) > number:
        print('Твое число больше загаданного мной.')

    if int(x) == number:
        print('Ух ты! Ты угадал мое число, использовав {} попыток!'.format(number_attempts))
        break