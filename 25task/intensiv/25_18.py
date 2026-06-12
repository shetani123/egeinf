def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x == 0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(550_001, 551_000):
    d = [x for x in div(i) if x % 10 == 7]
    if len(d) == 3:
        print(i,max(d))