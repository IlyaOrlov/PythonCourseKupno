# Часто задача программиста заключается в том, чтоб найти в документации
# готовую функцию, которая реализует необходимое решение. Данное задании
# предполагает самостоятельное изучение документации к библиотеке itertools
# (это набор готовых итераторов), чтобы подобрать те функции, которые дадут
# правильные ответы на следующие вопросы (иногда надо будет добавить свои аргументы
# при вызове функций помимо тех, что указаны в задании):


import itertools


# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]),
# а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])

def chain(lst1, lst2, lst3):
    a = itertools.chain(lst1, lst2, lst3)
    return list(a)

my_lst1 = [1,2,3]
my_lst2 = [4,5]
my_lst3 = [6,7]

a = chain(my_lst1, my_lst2, my_lst3)
print(a)


# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code'])
# и возвращает массив из элементов, у которых длина не меньше пяти (['hello', 'write'])

def false(lst):
    a = itertools.filterfalse(lambda x: len(x) < 5, lst)
    return list(a)

my_lst = ['hello', 'i', 'write', 'cool', 'code']

a = false(my_lst)
print(a)



# Функция выдает на строку 'password' все возможные комбинации вида
# ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)

def combinations(stroka):
    a = itertools.combinations(stroka, 4)
    return list(a)

my_str = 'password'

a = combinations(my_str)
print(a)
