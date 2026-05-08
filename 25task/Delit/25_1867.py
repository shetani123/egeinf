def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(500_000,500_100):
    d = [x for x in div(i) if x != 8]
    if any(n % 10 == 8 for n in d):
        print(i, [n for n in d if n % 10 == 8])