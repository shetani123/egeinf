s = open('24_4643.txt').readline()

m = 0

s = s.replace("11A", "F").replace("11B", "F").replace("12A", "F").replace("12B", "F").replace("22A", "F").replace("22B", "F").replace("21A", "F").replace("21B", "F")

for i in range(len(s)):
    for j in range(i, len(s)):
        c = s[i:j+1]
        if "A" not in c and "B" not in c and "1" not in c and "2" not in c:
            m = max(m, len(c))
        else:
            break
print(m)