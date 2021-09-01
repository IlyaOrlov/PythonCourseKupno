def sort(a):
    for i in range(len(a) - 1):
        x = i
        for y in range(i + 1, len(a)):
            if a[y] < a[x]:
                x = y
        a[i], a[x] = a[x], a[i]

s = list(input())

print(s)
sort(s)
print(s)
