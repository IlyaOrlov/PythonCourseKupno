import random

def del_column(lst, x):
    for i in range(len(lst)):
        for j in reversed(range(len(lst[i]))):
            if lst[i][j] == x:
                for k in range(len(lst)):
                    del lst[k][j]

lst = [
    [1, 1, 2],
    [1, 2, 1],
    [1, 1, 1]
]

print(*lst, sep='\n')
x = int(input('Введите число: '))
del_column(lst, x)
print(*lst, sep='\n')

row = int(input('Введите кол-во строк: '))
column = int(input('Введите кол-во столбцов: '))
lst1 = [[random.randrange(1, 10) for _ in range(column)] for _ in range(row)]
print(*lst1, sep='\n')
x = int(input('Введите число: '))
del_column(lst1, x)
print(*lst1, sep='\n')
