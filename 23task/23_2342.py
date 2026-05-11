def F(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        if x % 10 == 9:
            z = int(str(x // 10 + 1) + str(x % 10))
            return F(z,y)+F(x+1,y)
        else:
            z = int(str(x // 10 + 1) + str(x % 10 + 1))
            return F(z,y)+F(x+1,y)
print(F(25,51))
