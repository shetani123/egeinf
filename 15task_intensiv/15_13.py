def f(x,y,z):
    return ((z % 115 == 0) and (y % 78 == 0) and (x % 51 == 0)) <= ((x*y*z) % A == 0)

for A in range(1,10**11):
    if all(f(x,y,z) for x in range(51,10**3,51) for y in range(78,10**3,78) for z in range(115,10**3,115)):
        print(A)