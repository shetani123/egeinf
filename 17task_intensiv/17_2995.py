a = [int(x) for x in open('17_2995.txt')]

sr = sum([x for x in a])/len(a)
k = 0
maxi = 0

for i in range(len(a)-1):
    if a[i] < sr and a[i+1] < sr:
        if a[i] % 10 == 9 or a[i+1] % 10 == 9:
            k += 1
            if maxi < a[i]+a[i+1]:
                maxi = a[i]+a[i+1]
print(k,maxi)