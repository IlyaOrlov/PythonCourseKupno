def my_gen(arg):
    for x in arg:
        yield x ** 2


lst = [1, 2, 3]

gen = my_gen(lst)

print(list(gen))

for i in gen:
    print(i)


