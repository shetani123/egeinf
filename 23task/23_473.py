def F(x,y):
    if x == y:
        return 1
    if x > y or x == 43:
        return 0
    if x < y:
        return F(x+2,y) + F(x + x + 1,y) +F(x + x - 1,y)
print(F(7,63))