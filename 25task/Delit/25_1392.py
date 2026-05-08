def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(550_000, 551_000):
    d = div(i)
    if len(d) > 0 and (sum(d) // len(d)) % 31 == 13:
        print(i, sum(d) // len(d))