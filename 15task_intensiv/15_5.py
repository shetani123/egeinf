def f(x,y):
    return (x < A) or (y < A) or (x + 2*y > 150)

for A in range(1,10**5):
    if all(f(x,y) for x in range(1,10**4) for y in range(1,10**4)):
        print(A)
