f1 = 'sourse.txt'
f2 = 'destination.txt'
try:
    file1 = open('sourse.txt', 'r')
    textfile1 = file1.read()
except Exception:
   print("Файл " + f1 + " не найден")
else:
    try:
        file2 = open('destination.txt', 'w')
        file2.write(textfile1)
    except Exception:
        print("Файл " + f2 + " используется")
    print(textfile1)
    file1.close()
    file2.close()
    file2 = open('destination.txt', 'r')
    textfile2 = file2.read()
    print(textfile2)
    file2.close()