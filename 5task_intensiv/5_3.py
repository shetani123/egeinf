m = []

for n in range(1,300):
    r = bin(n)[2:]
    if n % 5 == 0:
        r = r + '1'
    else:
        r = r + bin(((n%5)*2))[2:]
    if int(r,2) > 102:
        m.append(int(r,2))
print(min(m))