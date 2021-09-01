def sort(a):
    for i in range(len(a) - 1):
        x = i
        y = i + 1
        while y < len(a):
            if a[y] < a[x]:
                x = y
            y = y + 1
        a[i], a[x] = a[x], a[i]

s = list(input())

print(s)
sort(s)
print(s)
