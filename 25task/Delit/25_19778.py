def div(a):
    d = set()
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.add(x)
            d.add(a//x)
    return sorted(d)

for i in range(9_500_000,9_510_000):
    d = [x for x in div(i) if x > 1 and all(x % y != 0 for y in range(2,int(x**0.5)+1)) and x != i]
    if len(d) > 0 and (sum(d) // len(d)) % 813 == 0:
        print(i, sum(d) // len(d))