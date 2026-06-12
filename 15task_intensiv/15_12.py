def f(x):
    return (x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0))

for A in range(1,10**6):
    if all(f(x) for x in range(1,10**6)):
        print(A)