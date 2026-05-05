def div(a):
    d = set()
    for x in range(1,int(a**0.5)):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(300_000, 301_000):
    d = [x for x in div(i) if x % 3 == 0 and x != i]
    if len(d) == 5:
        print(i, [x for x in d if x % 3 == 0])
