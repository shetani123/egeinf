from functools import lru_cache
@lru_cache(maxsize=None)
def f(x):
    if x == 1: return 1
    if x > 1:
        return x**2 + f(x-1)
for i in range(1,1000):f(i)
print(f(1000)-f(997))