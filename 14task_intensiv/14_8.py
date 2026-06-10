for x in range(1,2030):
    n = 6**260 + 6**160 + 6**60 - x
    n6 = ''
    while n > 0:
        n6 = str(n%6) + n6
        n //= 6
    if n6.count("0") == 202:
        print(x)