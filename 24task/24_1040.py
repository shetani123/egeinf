s = open("24_1040.txt").readline()

m = 1

for i in "qwertyuiopasdfghjklzxcvbnm":
    s = s.replace(i,"A")

for l in range(len(s)):
    for r in range(l,len(s)):
        c = s[l:r+1]
        if "A" not in c:
            if len(c) > m:
                m = len(c)
        else:
            break
print(m)