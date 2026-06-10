n = 2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35
n49 = []
k = 0
while n > 0:
    n49.append(str(n%49))
    n = n // 49
for i in n49:
    if int(i) < 9:
        k += 1
print(k)