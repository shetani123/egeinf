m = []
for n in range(1,200):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r + '0'
    else:
        r = '1' + r + '10'
    if int(r,2) > 320:
        m.append(int(r,2))
print(min(m))