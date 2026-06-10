clA = [[],[]]
clB = [[],[],[]]

for s in open("27A_25439.txt"):
    x, y = [float(d) for d in s.split()]
    if x > 40 or y > 30:
        pass
    elif 15 < y < 25 and 0 < x < 10:
        clA[0].append([x, y])
    elif 5 < y < 15 and 0 < x < 10:
        clA[1].append([x, y])

for s in open("27B_25439.txt"):
    x, y = [float(d) for d in s.split()]
    if y > 6 or x < -2:
        pass
    elif -2 < x -1:
        clB[0].append([x, y])
    elif y < 5 and x < 0:
        clB[1].append([x, y])
    elif 5 < y < 6:
        clB[2].append([x, y])

from math import dist

def center(c):
    m = []
    for p in c:
        s = sum(dist(p,p1) for p1 in c)
        m.append([s,p])
    return min(m)[1]

x0 , y0 = center(clA[0])
x1, y1 = center(clA[1])
print(int(min(x0,x1)*10000), int(min(y0,y1)*10000))
print(min(
    len(clB[0]),
    len(clB[1]),
    len(clB[2])
),max(
    len(clB[0]),
    len(clB[1]),
    len(clB[2])
), )
