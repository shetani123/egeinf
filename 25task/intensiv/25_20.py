def div(a):
    d = set()
    for i in range(1,int(a**0.5)+1):
        if a % i == 0:
            d.add(i)
            d.add(a//i)
    return sorted(d)

for i in range(1,100_000):
    d = [x for x in div(i+750_000) if x % 2 ==0]
    if len(d) % 2 != 0:
        print(i,len(d))