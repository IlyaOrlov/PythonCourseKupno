def tab_space(x):
    if x == 'tab':
        with open('text.txt', 'r') as f, \
                open('text_tab.txt', 'w') as f_tab:
            for line in f:
                line_w_tabs = line.replace('    ', '\t')
                print(line_w_tabs)
                f_tab.write(line_w_tabs)
    else:
        with open('text.txt', 'r') as f, \
                open('text_space.txt', 'w') as f_space:
            for line in f:
                line_w_space = line.replace('\t', '    ')
                print(line_w_space)
                f_space.write(line_w_space)

with open('text.txt', 'w') as f:
    f.write(input('Введите текст '))

x = input('Если хотите поменять пробелы на табуляцию, то введите tab, если же наоборот, то введите space')

while True:
    if x == 'tab':
        tab_space(x)
        break
    elif x == 'space':
        tab_space(x)
        break
    else:
        print('Введите tab или space')