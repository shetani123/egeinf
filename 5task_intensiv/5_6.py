m = []

for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r + '10'
    else:
        r = '1' + r + '00'
    if int(r,2) > 100:
        m.append(int(r,2))
print(min(m))