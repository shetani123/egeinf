clA = [[],[],[],[],[]]

for s in open('27_A(3).txt'):
    x,y = s.split()
    x, y = float(x),float(y)
    if 0 < x < 20 and y > 40:
        clA[0].append([x,y])
    elif 0 < x < 20 and y < 20:
        clA[1].append([x,y])
    elif 20 < x < 40 and 20 < y < 40:
        clA[2].append([x,y])
    elif 40 < x < 65 and y > 40:
        clA[3].append([x,y])
    elif 40 < x < 65 and y < 20:
        clA[4].append([x,y])
clB = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for s in open('27_B(3).txt'):
    x,y = s.split()
    x, y = float(x),float(y)
    if y > 60 and 20 < x < 30:
        clB[0].append([x,y])
    elif y > 55 and 40 < x < 55:
        clB[1].append([x,y])
    elif 50 < y < 60 and 5 < x < 20:
        clB[2].append([x,y])
    elif 50 < y < 60 and 20 < x < 30:
        clB[3].append([x,y])
    elif 35 < y < 50 and 5 < x < 20:
        clB[4].append([x,y])
    elif 35 < y < 50 and 25 < x < 35:
        clB[5].append([x,y])
    elif 35 < y < 50 and 35 < x < 50:
        clB[6].append([x,y])
    elif 30 < y < 40 and 50 < x < 60:
        clB[7].append([x,y])
    elif 40 < y < 55 and 60 < x < 70:
        clB[8].append([x,y])
    elif 20 < y < 30 and 5 < x < 20:
        clB[9].append([x,y])
    elif 25 < y < 35 and 25 < x < 35:
        clB[10].append([x,y])
    elif 25 < y < 35 and 35 < x < 48:
        clB[11].append([x,y])
    elif 20 < y < 30 and 50 < x < 60:
        clB[12].append([x,y])
    elif 5 < y < 17 and 5 < x < 17:
        clB[13].append([x,y])
    elif 5 < y < 17 and 20 < x < 30:
        clB[14].append([x,y])
    elif 5 < y < 17 and 35 < x < 47:
        clB[15].append([x,y])
    elif 0 < y < 15 and 54 < x < 62:
        clB[16].append([x,y])
    elif 5 < y < 20 and 62 < x < 70:
        clB[17].append([x,y])

def dist(p,p1):
    x0,y0 = p
    x1,y1 = p1
    return ((x1-x0)**2 + (y1-y0)**2)**0.5
def anticent(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return max(m)[1]

for i in range(0,5):
    print(len(clA[i]), end=' ')
print(end = '\n')
c = anticent(clA[1])
c1 = anticent(clA[2])
print(int(((c[0]+c1[0])/2)*10_000), int(((c[1]+c1[1])/2)*10_000))

for i in range(0,18):
    print(len(clB[i]), end=' ')
print(end = '\n')
c10 = anticent(clB[10])
c13 = anticent(clB[13])
c16 = anticent(clB[16])
print(
    int(((c10[0]+c13[0]+c16[0])/3)*10_000),int(((c10[1]+c13[1]+c16[1])/3)*10_000)
)