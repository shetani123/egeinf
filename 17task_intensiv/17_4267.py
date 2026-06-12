a = [int(x) for x in open('17_4267.txt')]

mx = max([x for x in a if x % 22 == 0])
k = 0
mini = 99999

for i in range(len(a)-1):
    if a[i] > mx or a[i+1] > mx:
        k += 1
        if mini > a[i] + a[i+1]:
            mini = a[i] + a[i+1]
print(k,mini)