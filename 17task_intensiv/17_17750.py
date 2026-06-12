a = [int(x) for x in open('17_17750.txt')]

mini = min([x for x in a])

k = 0
maxi = 0

for i in range(len(a)-1):
    if a[i] % 77 + a[i+1] % 77 == mini:
        k += 1
        if maxi < a[i] + a[i+1]:
            maxi = a[i] + a[i+1]
print(mini)
print(k, maxi)