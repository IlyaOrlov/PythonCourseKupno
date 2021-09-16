import functools


def mysum(a, b):
    return a + b


mysum1 = functools.partial(mysum, b=100)
# mysum1 = lambda a: mysum(a, b=100)
print(mysum1(50))


