a = [int(x) for x in open('17_7619.txt')]

m = max(x for x in a if 10 <= x <= 99)

k = 0

maxi = 0
for i in range(len(a)-1):
    if (len(str(a[i])) == 2 or len(str(a[i+1])) == 2) and (a[i] + a[i+1]) % m == 0:
        k += 1
        if a[i] + a[i+1] > maxi:
            maxi = a[i] + a[i+1]
print(k, maxi)