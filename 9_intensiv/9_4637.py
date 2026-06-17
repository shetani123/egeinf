k = 0
for s in open('9_4637.csv'):
    n = sorted(map(int, s.split()))
    if n[3]**3 >= (n[0]*n[1]*n[2])*2 and n[0] > 10 and n[1] > 10 and n[2] > 10 and n[3] > 10:
        k = k + 1
print(k)