for x in range(1,2000):
    n = 125**200 - 5**x + 74
    n5 = ''
    while n > 0:
        n5 = str(n%5) + n5
        n //= 5
    if n5.count("4") == 100:
        print(x)
        break