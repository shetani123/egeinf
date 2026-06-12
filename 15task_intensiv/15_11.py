def f(x):
    return ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (A <= x)

for A in range(1,10**6):
    if all(f(x) for x in range(1,10**5)):
        print(A)