def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(154026,154044):
    d = div(i)
    if len(d) == 4:
        print(d[2],d[3])