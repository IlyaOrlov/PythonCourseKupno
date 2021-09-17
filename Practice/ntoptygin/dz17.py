#Функции на вход подаётся последовательность чисел source и множитель m.
# На выходе функции ожидается новая последовательность на основе source,
# где каждый член был умножен на m. Если source не был указан, то берётся
# последовательность [1,2,3]. Укажите ошибки, допущенные в данной функции,
# и предложите свою реализацию

import copy

def multiplier(m=1, source=[1,2,3]):
    result = []
    for i, x in enumerate(source):
        result.append(source[i] * m)
    return result

lst = [1,2,4]

a = multiplier(5,lst)
print(a)
a = multiplier(5,lst)
print(a)

# проблема была в том, что функция multiplier изменяла наш исходный список