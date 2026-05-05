def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(190_201, 190_261):
    d = [x for x in div(i) if x % 2 == 0]
    if len(d) == 4:
        print(d[3],d[2])