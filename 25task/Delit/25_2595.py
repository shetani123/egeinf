def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(400_000_000,400_100_000):
    d = div(i)
    if len(d) >= 5 and (d[0] * d[1] * d[2] * d[3] * d[4]) % 100 == 17 and (d[0] * d[1] * d[2] * d[3] * d[4]) < i:
        print(d[0] * d[1] * d[2] * d[3] * d[4], d[4])