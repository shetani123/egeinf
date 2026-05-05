s = open("24_21.txt").readline()

m = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        c = s[i:j+1]
        if "XX" not in c and "YY" not in c and "ZZ" not in c:
            m = max(m, len(c))
        else:
            break
print(m)