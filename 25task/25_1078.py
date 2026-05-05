def div(a):
    d = set()
    for x in range(2,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(1_204_300, 1_204_381):
    d = [x for x in div(i) if x % 2 == 0]
    if len(d) > 0 and sum(d) % 10 == 0:
        print(i, sum(d))