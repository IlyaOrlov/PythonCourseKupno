import time
import functools


@functools.lru_cache(maxsize=None)
def factorial(n):
    print(f'factorial called for {n}')
    return n * factorial(n-1) if n else 1


t = time.time()
print(factorial(20))
print(factorial(10))
print(f'Total time: {time.time() - t}')
