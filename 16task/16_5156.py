from functools import lru_cache
from sys import *
setrecursionlimit(10**9)
@lru_cache(maxsize=None)
def f(x):
    if x <= 3:
        return x
    if x > 3 and x % 2 != 0:
        return 2*x + f(x-2)
    if x > 3 and x % 2 == 0:
        return x**2 + f(x-1)

for i in range(1,10000):f(i)
print(f(10_000)-f(9_995))