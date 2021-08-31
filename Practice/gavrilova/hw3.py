def fun(a):
    y = y.join(a)
    print(a)


def get_arg(arg):
     while not arg.lower() == "stop":
        arg = input('Введите число ')
        if arg.isnumeric():
            x.append(arg)

        else:
            if arg == "stop":
#                break
                pass
#                 continue
            else:
                print("Некорректный ввод")
     return x


  #  print(arg)

y = ''
x = []
x = get_arg('x')
y = y.join(x)
print(y)
#fun(x)

