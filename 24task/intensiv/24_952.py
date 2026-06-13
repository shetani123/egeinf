s = open('24_952.txt').readline()

m = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if c.count('A') == 0 and c.count('E') == 0:
            m = max(m,len(c))
        else:
            break
print(m)