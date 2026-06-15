clA = [[],[]]
clB = [[],[],[]]
for s in open('27A_18054.txt'):
    x,y = s.split()
    x ,y = float(x),float(y)
    if x < 3:
        clA[0].append([x,y])
    if x > 3:
        clA[1].append([x,y])
for s in open('27B_18054.txt'):
    x,y = s.split()
    x ,y = float(x),float(y)
    if y > -2.5 and x < 3.5:
        clB[0].append([x,y])
    elif y < -2.5:
        clB[1].append([x,y])
    elif y > -2.5 and x > 3.5:
        clB[2].append([x,y])
def dist(p,p1):
    x1,y1 = p
    x2,y2 = p1
    return max(abs(x2-x1), abs(y2-y1))

def cent(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]
c0 = cent(clA[0])
c1 = cent(clA[1])
print(
    int(((c0[0]+c1[0])/2)*10_000),int(((c0[1]+c1[1])/2)*10_000)
)
c2 = cent(clB[0])
c3 = cent(clB[1])
c4 = cent(clB[2])
print(c2,c3,c4)
print(
    int(((c2[0]+c3[0]+c4[0])/3)*10_000),int(((c2[1]+c3[1]+c4[1])/3)*10_000)
)