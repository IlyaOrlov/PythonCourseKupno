def my_enumerate(seq):
    new_lst = []
    i = 0
    for each in seq:
        new_lst.append((i, each))
        i += 1
    return new_lst


x = {"a", "b", "c"}

for i in my_enumerate(x):
    print(i)
