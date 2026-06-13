def tri(x):
    tri3 = ''
    while x > 0:
        tri3 = str(x%3) + tri3
        x //= 3
    return tri3

m = []

for n in range(1,1000):
    r = tri(n)
    if r[-2:] == '10':
        r = '2' + r
    else:
        r = '1' + r
    if int(r,3) > 130:
        m.append(n)
print(min(m))