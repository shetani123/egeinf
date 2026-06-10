for x in range(1,5556):
    n = 5**150 + 5**135 - x
    n5 = ""
    while n > 0:
        n5 = str(n%5) + n5
        n //= 5
    if n5.count("4") == 134:
        print(x)