k = 0
for s in open('09_17356.csv'):
    n = sorted(map(int,s.split(',')))
    if n[0]**2 + n[4]**2 > (n[1]+n[2]+n[3])**2:
        k += 1
print(k)