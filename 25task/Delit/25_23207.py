def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(1_324_728, 1_325_727):
    d = [x for x in div(i) if x > 1 and all(x % y != 0 for y in range(2, int(x ** 0.5) + 1)) and x != i]
    if len(d) == 2 and d[0] * d[1] == i and str(d[0]).count('5') == 1 and str(d[1]).count('5') == 1:
        print(i,max(d[0], d[1]))
    if len(d) == 1 and d[0]**2 == i and str(d[0]).count('5') == 1:
        print(i,d[0])