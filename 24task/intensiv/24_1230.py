s = open('24_1230.txt').readline()

m = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if c.count('W') == 0 and c.count('R') == 0 and c.count('Q') == 0:
            m = max(m,len(c))
        else:
            break
print(m)