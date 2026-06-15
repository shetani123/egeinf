clA = [[],[]]
clB = [[],[],[]]
for s in open('27_A_29076.txt'):
    x ,y ,t = s.split()
    x ,y  = float(x),float(y)
    if y < 8:
        clA[0].append([x,y,t])
    elif y > 8:
        clA[1].append([x,y,t])
for s in open('27_B_29076.txt'):
    x ,y ,t = s.split()
    x ,y = float(x),float(y)
    if y > 22:
        clB[0].append([x,y,t])
    elif y < 22 and x < 20:
        clB[1].append([x,y,t])
    elif y < 22 and x > 20:
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

k1 = []
k2 = []
for i in clA[0]:
    if i[2][1] == '2':
        k1.append(i)
for i in clA[1]:
    if i[2][1] == '2':
        k2.append(i)
print(len(k1),len(k2))
c = cent(clA[0])
c1 = cent(clA[1])
print(
    int((c1[0]*10_000)),int((c[1]*10_000))
)
kr1 = []
kr2 = []
kr3 = []
for i in clB[0]:
    if i[2][0] == 'Y':
        kr1.append(i)
for i in clB[1]:
    if i[2][0] == 'Y':
        kr2.append(i)
for i in clB[2]:
    if i[2][0] == 'Y':
        kr3.append(i)
print(len(kr1),len(kr2), len(kr3))
c2 = cent(clB[1])
c3 = cent(clB[2])
c4 = cent(clB[0])
print(int(dist(c2,c3)*10_000))
distkr2 = [dist(x,c2) for x in kr2]
distkr3 = [dist(x,c3) for x in kr3]
distkr1 = [dist(x,c4) for x in kr1]
print(int(max(distkr2)*10_000),int(max(distkr3)*10_000),int(max(distkr1)*10_000))