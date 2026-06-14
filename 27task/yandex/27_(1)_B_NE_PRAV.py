clA = [[],[]]
clB = [[],[],[]]
for s in open('27_А(1).txt'):
    x, y = s.split()
    x, y = float(x), float(y)
    if y < 10:
        clA[0].append([x,y])
    elif y > 15:
        clA[1].append([x,y])
for s in open('27_Б(1).txt'):
    x, y = s.split()
    x, y = float(x), float(y)
    if 9 <= x <= 19 and 8 <= y <= 14:
        clB[0].append([x,y])
    elif y > 14 and 13 <= x <= 21:
        clB[1].append([x,y])
    elif 21 <= x <= 31 and 0 < y <= 12:
        clB[2].append([x,y])
def dist(p,p1):
    x1,y1 = p
    x2,y2 = p1
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
def cent(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

c = cent(clA[0])
c1 = cent(clA[1])
print(int((c[0]+c1[0])*10_000), int((c[1]+c1[1])*10_000))

t1 = []
for i in clB[0]:
    t1.append([dist(i,p) for p in clB[1]])
    t1.append([dist(i, p) for p in clB[2]])
for i in clB[1]:
    t1.append([dist(i, p) for p in clB[0]])
    t1.append([dist(i, p) for p in clB[2]])
for i in clB[2]:
    t1.append([dist(i, p) for p in clB[0]])
    t1.append([dist(i, p) for p in clB[1]])
print(len(clB[0]), len(clB[1]), len(clB[2]))
print(min(int(min(t1)[0]*10_000),int(min(t1)[1]*10_000),int(min(t1)[2]*10_000)))
print(max(int(max(t1)[0]*10_000),int(max(t1)[1]*10_000),int(max(t1)[2]*10_000)))