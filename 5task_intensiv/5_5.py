m = []

for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '10' + r + '1'
    if int(r,2) < 1000:
        m.append(n)
print(max(m))