def wrapper(fun):
    def newfun(a, b):
        print("Before additional features")
        fun(a, b)
        print("After additional features")
    return newfun


def benchmark(func):
    """
    Обертка для подсчета времени выполнения функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print(f"{func.__name__} spent {time.perf_counter() - t}")
        return res
    return wrapper


@benchmark
@wrapper
def somefun(a, b):
    print(f'Got arguments {a} and {b}')
    return a + b


#somefun = wrapper(somefun)

somefun(20, 30)
