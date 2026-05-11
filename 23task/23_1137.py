def F(x,y):
    if x == y:
        return 1
    if int(x,2) > int(y,2):
        return 0
    if int(x,2) < int(y,2):
        return F(bin(int(x,2)+1)[2:], y) + F(x + '0', y) + F(x + '1',y)
print(F('100', '11101'))