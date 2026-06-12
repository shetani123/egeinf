def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x == 0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(250_200, 251_200):
    d = div(i)
    if len(d) >= 2:
        if (max(d)+min(d)) % 123 == 17:
            print(i, max(d)+min(d))