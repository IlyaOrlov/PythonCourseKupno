f1 = 'sourse.txt'
f2 = 'destination.txt'
try:
    with open(f1, 'r') as file1:
#    file1 = open(f1, 'r')
        textfile1 = file1.read()
except Exception:
    print(f'Файл {f1} не найден')
#   print("Файл " + f1 + " не найден")
else:
    try:
        with open(f2, 'r') as file2:
            print(f'Файл {f2} уже существует')
#        file2 = open(f2, 'w')
#            file2.write(textfile1)
    except Exception:
        with open(f2, 'w') as file2:
            file2.write(textfile1)
    print(textfile1)
#    file1.close()
#    file2.close()
    with open(f2, 'r') as file2:
#    file2 = open(f2, 'r')
        textfile2 = file2.read()
        print(textfile2)
#    file2.close()