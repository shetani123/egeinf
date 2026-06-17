for s in open('9_12918.csv'):
    a = sorted(map(int, s.split()))
    a2 = [x for x in a if a.count(x) == 2]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a2) == 4 and len(a1) == 2 and a.count(a[5]) == 1 and max(a)*min(a)>a[1]+a[2]+a[3]+a[4]:
        print(sum(a))
        break
