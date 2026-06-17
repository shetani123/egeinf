k = 1
for s in open('9_23268.csv'):
    a = sorted(map(int, s.split()))
    a2 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2) == 4 and sum(a2)/4 < max(a1) and len(a1) == 3:
        print(k)
        break
    k += 1