import random

def del_column(lst):
    x = int(input('Введите число: '))
    for j in reversed(range(column)):
        for i in range(row):
            if lst[i][j] == x:
                for k in range(row):
                    del lst[k][j]
row = int(input('Введите кол-во строк: '))
column = int(input('Введите кол-во столбцов: '))
lst = [[random.randrange(1, 10) for _ in range(column)] for _ in range(row)]
print(*lst, sep='\n')
del_column(lst)
print(*lst, sep='\n')
