s = open("24_2422.txt").readline()

m = 0

for i in range(1,len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if c[i] >= c[i-1]:
            m = max(m,len(c))
print(m)