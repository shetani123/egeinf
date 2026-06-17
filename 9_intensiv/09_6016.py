k = 0
for s in open('09_6016.csv'):
    n = sorted(map(int, s.split()))
    if n[0] != n[1] != n[2] and n[2]**2 < n[0]**2 + n[1]**2:
        k += 1
print(k)