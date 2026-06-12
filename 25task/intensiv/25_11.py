def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x == 0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(1_204_300, 1_204_380):
    d = [i for i in div(i) if i % 2 == 0]
    S = sum(d)
    if S != 0 and S % 10 == 0:
        print(i,S)
