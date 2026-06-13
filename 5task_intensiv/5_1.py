for i in range(1,100):
    n = bin(i)[2:]
    s1 = sum([int(i) for i in n])
    n = n + str(s1 % 2)
    s2 = sum([int(i) for i in n])
    n = n + str(s2 % 2)
    if int(n,2) > 80:
        print(i,int(n,2))