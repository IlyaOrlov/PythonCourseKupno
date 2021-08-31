lst = []
a = 0

while True:
    a = input('Введите число: ')
    if a.isnumeric():
        lst.append(a)
    elif a.lower() == 'stop':
        break
    else:
        print ('Нужно ввести только число или команду stop')

b = ''.join(lst)
print (b)