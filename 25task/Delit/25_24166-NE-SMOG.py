def div(a):
    d = []
    for x in range(1,int(a**0.5)+1):
        if a % x ==0:
            d.append(x)
            d.append(a//x)
    return sorted(d)

def pal(d):
    a = sum(d)
    for i in range(len(d)//2):
        if d[i] == d[-i]:
            return True

for i in range(7_305_679, 7_306_679):
    d = [x for x in div(i) if x > 1 and all(x % y != 0 for y in range(2, int(x ** 0.5) + 1)) and x != i]
    if len(d) == 4 and d[0]*d[1]*d[2]*d[3] == i and pal(d):
        print(i,sum(d))
    elif len(d) == 3  and (d[0]*d[1]*d[2]**2 == i or d[0]*d[1]**2*d[2] == i or d[0]**2*d[1]**d[2] == i) and pal(d):
        print(i,sum(d))
    elif len(d) == 2 and (d[0]**2*d[1] == i or d[0]*d[1]**2 == i) and pal(d):
        print(i,sum(d))
    elif len(d) == 1 and d[0]**4 == i and pal(d):
        print(i,sum(d))

