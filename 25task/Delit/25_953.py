def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(500_000,1,-1):
    d = [x for x in div(i) if x > 1 and all(x % y != 0 for y in range(2,int(x**0.5)+1)) ]
    if len(d) > 0 and sum(d) % 10 == 0:
        print(i,sum(d))