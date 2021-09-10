def multiplier(m=1, source=[1, 2, 3]):
    return [source[i] * m for i, x in enumerate(source)]

print(multiplier(5))
print(multiplier(2))
