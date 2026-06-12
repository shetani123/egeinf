def f(x,y):
    return (11 <= y) or (7*y < x) or (A > x * y)

for A in range(1, 10**5):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(A)