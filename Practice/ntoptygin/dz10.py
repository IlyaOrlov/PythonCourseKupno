# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции
# в файле или строке. То есть, передается на вход файл или строка, необходимо заменить все символы
# табуляции на четыре пробела, либо же заменить все комбинации из четырех символов пробела на
# символ табуляции

import os

with open('text.txt', 'w') as f:
    f.write(input('Введите текст '))

a = None

while not (a == 'space' or a == 'tab' ):
    a = input('Введите, что Вы хотите сделать. Если заменить табуляцию на пробелы - нажмите tab. \
Если заменить пробелы на табуляцию - space. ')
    with open('text.txt', 'r') as f, \
             open('new_text.txt', 'w') as nf:
        for line in f:
            if a == 'space':
                line = line.replace('    ', '\t')
            elif a == 'tab':
                line = line.replace('\t', '    ')
            else:
                print('Нужно было ввести space или tab', end='')
            print(line)
            nf.write(line)



os.remove('text.txt')
os.rename('new_text.txt', 'text.txt')