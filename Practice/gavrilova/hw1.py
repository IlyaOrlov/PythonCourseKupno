def test1(a, b): # вывод на экран большего значения из двух чисел
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("Числа равны")

def test2(a, b): # возврат бол7ьшего значения из двух чисел
     if a > b:
         return(a)
     elif a < b:
         return(b)
     else:
         return(None)

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

test1(a,b)
#test2(a,b)

x = test2(a,b) #проверка возврвщаемого значения
print(x)