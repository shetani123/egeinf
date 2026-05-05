s = open('24_8510.txt').readline()

m = 0

for i in range(len(s)):
    for j in range(i,len(s)):
        c = s[i:j+1]
        if "NN" not in c and "OO" not in c and "PP" not in c and "NO" not in c and "NP" not in c and "ON" not in c and "OP" not in c and "PN" not in c and "PO" not in c:
            m = max(m,len(c))
        else:
            break
print(m)