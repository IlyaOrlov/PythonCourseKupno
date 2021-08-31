def fun(a):
    a = a + a
    print(a)


def get_arg(arg_name):
    #    While not (arg := input(f'Введите число {arg_name}: ')).isnumeric():
    ##    pass
    arg = input('Введите число ')
    while not arg.isnumeric():
        arg = input('Введите число ')
        if arg == "stop" or arg == "Stop" or arg == "STOP"
            break
        print("Некорректный ввод")

    returm
    arg


#    print(arg)

# x = None
x = get_arg('x')
fun(x)

# if x == 'stop':
#    print("OK)