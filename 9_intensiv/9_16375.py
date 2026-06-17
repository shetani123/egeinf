k = 0
for s in open('9_16375.csv'):
    a = sorted(map(int, s.split()))
    a2 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2) == 2 and len(a1) == 5:
        if a2[0]**2 < a1[0]*a[1]*a[2]:
            k += 1
print(k)