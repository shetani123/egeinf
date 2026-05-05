s = open("24_2423.txt").readline()

m = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if c[1] > c[0]:
            m = max(m,len(c))
        else:
            break
print(m)