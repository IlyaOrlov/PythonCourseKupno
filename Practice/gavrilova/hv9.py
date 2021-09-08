def fun(f, f_new, before, after):
    for line in f:
        line_new = line.replace(before, after)
        print(line_new)
        f_new.write(line_new)


with open('text.txt', 'w') as f:
    f.write(input('Введите строку '))


while True:
    x = input('Для замены пробелов на табуляцию введите t, для замены табуляции на пробелы введите s ')
    if x == 't':
        with open('text.txt', 'r') as f, \
                open('text_t.txt', 'w') as f_t:
            fun(f, f_t, '    ', '\t')
            break
    elif x == 's':
        with open('text.txt', 'r') as f, \
                open('text_s.txt', 'w') as f_s:
            fun(f, f_s, '\t', '    ')
            break
    else:
        print('Некорректный ввод')
