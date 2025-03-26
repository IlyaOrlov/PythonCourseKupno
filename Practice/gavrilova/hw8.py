def sort(a):
    for i in range(len(a)):
        n = i
#        print("i=",i)
        for j in range(i + 1,len(a)):
#            print("j=",j)
            if a[j] < a[n]:
                n = j
                a[i], a[n] = a[n], a[i]

аrr = list(input("Введите последовательность чисел "))

print(аrr)
sort(аrr)
print(аrr)