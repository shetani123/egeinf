def F(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        return F(x+2,y)+F(x+4,y)+F(x+5,y)
c = 0
for i in range(32,1000):
    c = F(31,i)
    if c == 1001:
        print(i)
        break
