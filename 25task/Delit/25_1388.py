def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(150_000, 151_000):
    d = div(i)
    if sum(d) % 13 == 10:
        print(i,  sum(d))