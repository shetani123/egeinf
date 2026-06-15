clA = [[],[],[],[]]
clB = [[],[],[],[],[]]
for s in open('27_A_17917.txt'):
    x ,y = s.split()
    x ,y = float(x),float(y)
    if y > 14:
        clA[0].append([x,y])
    elif 10 < y < 14 and 6 < x < 12:
        clA[1].append([x,y])
    elif 10 < y < 14 and x > 16:
        clA[2].append([x,y])
    else:
        clA[3].append([x,y])
for s in open('27_B_17917.txt'):
    x ,y = s.split()
    x ,y = float(x),float(y)
    if y > 10:
        clB[0].append([x,y])
    elif 5 < y < 8 and 20 < x < 25:
        clB[1].append([x,y])
    elif y < 4 and 0 < x < 10:
        clB[2].append([x,y])
    elif y < 5 and 22 < x < 28:
        clB[3].append([x,y])
    elif y < 4 and x > 28:
        clB[4].append([x,y])
def dist(p,p1):
    x1,y1 = p
    x2,y2 = p1
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
def cent(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]
c0 = cent(clA[0])
c1 = cent(clA[1])
c2 = cent(clA[2])
c3 = cent(clA[3])
print(
    int(((c0[0]+c1[0]+c2[0]+c3[0])/4)*10_000),int(((c0[1]+c1[1]+c2[1]+c3[1])/4)*10_000)
)
c4 = cent(clB[0])
c5 = cent(clB[1])
c6 = cent(clB[2])
c7 = cent(clB[3])
c8 = cent(clB[4])

print(
    int(((c4[0]+c5[0]+c6[0]+c7[0]+c8[0])/5)*10_000),int(((c4[1]+c5[1]+c6[1]+c7[1]+c8[1])/5)*10_000)
)