import cProfile

def fun(a, b):
    return a * b


with cProfile.Profile() as p:
    for i in range(100000):
        fun(5, i)
    p.print_stats(sort=True)
