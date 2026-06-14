clA = [[],[]]
clB = [[],[],[]]

for s in open('27_А.txt'):
    x,y,t = s.split()
    x,y = float(x), float(y)
    if y < 10:
        clA[0].append([x,y,t])
    elif y > 10:
        clA[1].append([x,y,t])

for s in open('27_Б.txt'):
    x,y,t = s.split()
    x,y = float(x), float(y)
    if x < 16 and y < 30:
        clB[0].append([x,y,t])
    elif x < 16 and y > 30:
        clB[1].append([x,y,t])
    elif x > 16:
        clB[2].append([x,y,t])

def dist(p,p1):
    x1,y1,t1 = p
    x2,y2,t2 = p1
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def cent(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return min(m)[1]

print(len(clA[0]), len(clA[1]))

c = cent(clA[0])
krg = []
for i in clA[0]:
    if i[2][0] == 'M' and i[2][2:] == 'III':
        krg.append([dist(i,c), i])
print(int(min(krg)[1][0]*10000),int(min(krg)[1][1]*10000))

org0 = []
org1 = []
org2 = []
yek0 = []
yek1 = []
yek2 = []
yekdist = []

for i in clB[0]:
    if i[2][0] == 'K' and i[2][2:] == 'III':
        org0.append(i)
for i in clB[1]:
    if i[2][0] == 'K' and i[2][2:] == 'III':
        org1.append(i)
for i in clB[2]:
    if i[2][0] == 'K' and i[2][2:] == 'III':
        org2.append(i)
print(len(org0), len(org1), len(org2))
c1 = cent(clB[0])
c2 = cent(clB[2])
print(int(dist(c1,c2)*10_000))

for i in clB[0]:
    if i[2][0] == 'G' and i[2][2:] == 'V':
        yek0.append(i)
for i in clB[1]:
    if i[2][0] == 'G' and i[2][2:] == 'V':
        yek1.append(i)
for i in clB[2]:
    if i[2][0] == 'G' and i[2][2:] == 'V':
        yek2.append(i)
for i in yek0:
    yekdist.append([dist(i,p) for p in yek0])
for i in yek1:
    yekdist.append([dist(i,p) for p in yek1])
for i in yek2:
    yekdist.append([dist(i,p) for p in yek2])

print(int(max(yekdist[1])*10_000))
