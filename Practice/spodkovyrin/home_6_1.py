def tab_space(f, f_tab_space, before, after):
    for line in f:
        line_w_change = line.replace(before, after)
        print(line_w_change)
        f_tab_space.write(line_w_change)
    # if x == 'tab':
    #     for line in f:
    #         line_w_tabs = line.replace('    ', '\t')
    #         print(line_w_tabs)
    #         f_tab_space.write(line_w_tabs)
    # else:
    #     for line in f:
    #         line_w_space = line.replace('\t', '    ')
    #         print(line_w_space)
    #         f_tab_space.write(line_w_space)

with open('text.txt', 'w') as f:
    f.write(input('Введите текст '))

x = input('Если хотите поменять пробелы на табуляцию, то введите tab, если же наоборот, то введите space: ')

while True:
    if x == 'tab':
        with open('text.txt', 'r') as f, \
                open('text_tab.txt', 'w') as f_tab:
            tab_space(f, f_tab, '    ', '\t')
            break
    elif x == 'space':
        with open('text.txt', 'r') as f, \
                open('text_space.txt', 'w') as f_space:
            tab_space(f, f_space, '\t', '    ')
            break
    else:
        print('Введите tab или space')
