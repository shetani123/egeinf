k = 0
for s in open('9_19228.csv'):
    a = sorted(map(int, s.split()))
    a4 = [x for x in a if a.count(x) == 4]
    a1 = [x for x in a if a.count(x) != 4]
    if len(a4) == 4 and a4[0]**2 < sum(a1):
        k += 1
print(k)