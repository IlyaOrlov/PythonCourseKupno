def fun(a):
    y = y.join(a)
    print(a)


def get_arg(arg):
     while not arg.lower() == "stop":
        arg = input('Введите число ')
        if arg.isnumeric():
            x.append(arg)

        elif arg != "stop":
            print("Некорректный ввод")
#        else:
#            if arg == "stop":
#                pass
#            else:
#                print("Некорректный ввод")
     return x


  #  print(arg)

y = ''
x = []
x = get_arg('x')
y = y.join(x)
print(y)
#fun(x)

