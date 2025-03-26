import random

x=0
number = random.randint(1, 10)

while True:
    x = input("Введите число в диапазоне от 1 до 10:")

    if not x.isnumeric():
        print("Вы ввели не число")
        break

    x = int(x)

    if x > number:
        print("Загаданное число меньше")
    elif x < number:
        print("Загаданное число больше")
    else:
#        x == number:
        print("Вы угадали")
        break