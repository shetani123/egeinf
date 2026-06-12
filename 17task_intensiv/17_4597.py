a = [int(x) for x in open('17_4597.txt')]

k = 0
maxi = 0

m = min([x for x in a])

for i in range(len(a)-1):
    if a[i] % 117 == m or a[i+1] % 117 == m:
        k += 1
        if maxi < a[i] + a[i+1]:
            maxi = a[i] + a[i+1]
print(k, maxi)