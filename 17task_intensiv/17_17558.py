a = [int(x) for x in open("17_17558.txt")]

suma = len([x for x in a if abs(x) % 32 == 0])

k = 0
maxi = -100_000

for i in range(len(a)-1):
    if (a[i] < 0 or a[i+1] < 0) and a[i]+a[i+1] < suma:
        k += 1
        if maxi < a[i]+a[i+1]:
            maxi = a[i]+a[i+1]
print(k,maxi)