def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a%x==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(350_001, 351_000):
    d = [x for x in div(i)]
    if len(d) > 0:
        if (max(d)-min(d)) % 23 == 9:
            print(i,max(d)-min(d))