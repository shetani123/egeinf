def f(x):
    return ((x % 12 == 0) <= (x % 42 != 0)) or (x + A >= 4096)

for A in range(1,10**6):
    if all(f(x) for x in range(1,10**5)):
        print(A)