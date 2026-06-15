from functools import lru_cache

@lru_cache(maxsize=None)
def f(x):
    if x == 1: return 1
    if x > 1:
        return x * f(x-1)
for i in range(1,1500):f(i)
print(f(2023)/f(2020))