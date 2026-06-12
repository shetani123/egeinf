def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x == 0 and x != 8:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(500_001, 501_000):
    d = [x for x in div(i) if x % 10 == 8]
    if len(d) > 0:
        print(i, d[0])