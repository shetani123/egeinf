s = open('24_4113.txt').readline()

s = s.replace('BB', 'F').replace('DD','F')

m = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        c = s[i:j+1]
        if "A" not in c and "B" not in c and "D" not in c:
            m = max(m,len(c))
        else:
            break

print(m)