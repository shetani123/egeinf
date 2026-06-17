k = 0
for s in open('9_3571.csv'):
    n = sorted(map(int,s.split()))
    if n[2]**2 > (n[0]*n[1])*2:
        k += 1
print(k)