s = open("24_4602.txt").readline()

m = 0

s = s.replace("BO", "F").replace("CO", "F").replace("DO", "F").replace("BA", "F").replace("CA", "F").replace("DA", "F")

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if "A" not in c and "B" not in c and "C" not in c and "D" not in c and "O" not in c:
            m = max(m,len(c))
        else:
            break
print(m)