lst = [1, 2, 3]
a = [x ** 2 for x in lst]
b = (x for x in range(100) if x % 2 == 0)

print(list(b))
print(list(b))

