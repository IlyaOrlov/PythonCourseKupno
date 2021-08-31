def test1(a, b): # вывод на экран большего значения из двух чисел
    if a > b:
        print(a)
    else:
        if a < b:
            print(b)
        else:
            return("Числа равны")

def test2(a, b): # возврат бол7ьшего значения из двух чисел
     if a > b:
         return(a)
     else:
         if a < b:
             return(b)
         else:
             print ("Числа равны")

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

test1(a,b)
test2(a,b)

# x = test2(a,b) #проверка возврвщаемого значения
# print x