s = open("24_4627.txt").readline()

m = 0

s = s.replace("NPO", "A").replace("PNO","A")

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if "N" not in c and "P" not in c and "O" not in c:
            m = max(m,len(c))
        else:
            break
print(m)