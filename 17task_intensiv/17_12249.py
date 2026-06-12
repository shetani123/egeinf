a = [int(x) for x in open('17_12249.txt')]

k = 0
maxi = 0
mx = max(x for x in a if len(str(abs(x))) == 5 and abs(x) % 10 == 3)
for i in range(len(a)-2):
    if abs(a[i]) % 10 == 3 or abs(a[i+1]) % 10 == 3 or abs(a[i+2]) % 10 == 3:
        if a[i] + a[i+1] + a[i+2] < mx:
            k += 1
            if maxi < a[i] + a[i+1] + a[i+2]:
                maxi = a[i] + a[i+1] + a[i+2]
print(k, maxi)