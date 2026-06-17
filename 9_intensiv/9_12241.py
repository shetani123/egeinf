k = 0
for s in open('9_12241.csv'):
    n = sorted(map(int, s.split()))
    a2 = [x for x in n if n.count(x) == 2]
    a1 = [x for x in n if n.count(x) == 1]
    if len(a2) == 6 and len(a1) == 1:
        if (a2[0] + a2[-1])/2 < a1[0]:
            k += 1
print(k)
