def tri(x):
    tri3 = ''
    while x > 0:
        tri3 = str(x % 3) + tri3
        x //= 3
    return tri3

m = []

for n in range(1,100):
    r = tri(n)
    if n % 5 != 0:
        r = r[:-1] + r[0] + tri(n%5)
    else:
        r = r + r[-1] + r[-1]
    if int(r,3) > 123:
        m.append(int(r,3))
print(min(m))