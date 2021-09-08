def sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] < a[j+1]:
                a[i], a[j+1] = a[j+1], a[i]

аrr = list(input("Введите последовательность чисел"))

print(аrr)
sort(аrr)
print(аrr)