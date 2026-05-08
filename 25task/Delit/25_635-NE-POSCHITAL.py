def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(107516162,152_673_837):
    d = div(i)
    if len(d) == 3:
        print(i,max(d))