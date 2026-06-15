from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**9)
@lru_cache()
def f(x):
    if x >= 10_000:
        return x
    if x < 10_000 and x % 3 == 0:
        return x + f(x//3)
    if x < 10_000 and x % 3 != 0:
        return 2*x + f( x+3)
for i in range(10_000,9_000,-1):f(i)