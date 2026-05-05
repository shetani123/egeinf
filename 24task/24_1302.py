s = open("24_1302.txt").readline()

m = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if "XZZY" not in c:
            m = max(m,len(c))
        else:
            break
print(m)