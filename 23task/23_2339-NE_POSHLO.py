def F(x,y,s):
    if x == y and s == 15:
        return 1
    if x == y and s != 15:
        return 0
    if x > y:
        return 0
    if x < y:
        return F(x*2,y, s + 1)+F(x*2 + 1, y, s +1)
for i in range(2**10,2**20):
    print(F(1,i,0))