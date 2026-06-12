def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a%x==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(150_001,151_000):
    s = sum([x for x in div(i)])
    if s > 0 and s % 13 == 10:
        print(i,s)