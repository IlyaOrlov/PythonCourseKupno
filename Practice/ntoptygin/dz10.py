# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции
# в файле или строке. То есть, передается на вход файл или строка, необходимо заменить все символы
# табуляции на четыре пробела, либо же заменить все комбинации из четырех символов пробела на
# символ табуляции




with open('text.txt', 'w') as f:
    f.write(input('Введите текст '))


a = None

while not a == 'space' or 'tab':
    a = input('Введите, что Вы хотите сделать. Если заменить табуляцию на пробелы - нажмите tab. Если заменить пробелы на табуляцию - space. ')
    if a == 'space':
        with open('text.txt', 'r+') as f:
            for line in f:
                line = line.replace('    ', '\t')
                print(line)
                f.write(line)
        break

    elif a == 'tab':
        with open('text.txt', 'r+') as f:
            for line in f:
                line = line.replace('\t', '    ')
                print(line)
                f.write(line)
        break

    else:
        print('Нужно ввести space или tab')