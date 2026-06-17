k = 1
for s in open('09_16962.csv'):
    a = sorted(map(int, s.split()))
    if a[0]+a[4] == a[1]+a[2]+a[3]:
        print(k)
    k += 1
print(1037-179)