from functools import lru_cache
from sys import *
setrecursionlimit(10**9)
@lru_cache(maxsize=10**9)
def f(x):
    if x > 100_000:
        return x
    if x <= 100_000:
        return f(x+1) + 5*x + 2
for i in range(100_001,1,-1): f(i)
print(f(3)-f(7))