def F(x,y,s):
    if x == y and s == 7:
        return 1
    if x ==y and s != 7:
        return 0
    if x > y:
        return 0
    if x < y:
        return F(x+1,y,s+1)+F(x+4,y,s+1)+F(x*2,y,s+1)
print(F(3,27,0))