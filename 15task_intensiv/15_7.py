def f(x,y):
    return (x >= 11) or ( 3 * x < y) or (x * y < A)

for A in range(10,10**3):
    if all(f(x,y)==1 for x in range(1000) for y in range(1000)):
        print(A)