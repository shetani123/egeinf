def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(55_000_000, 60_000_000):
    d = [x for x in div(i) if x % 2 != 0]
    if len(d) == 5:
        print(i,d)