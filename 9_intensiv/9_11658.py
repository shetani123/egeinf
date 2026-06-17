k = 1
for s in open('9_11658.csv'):
    a = sorted(map(int, s.split()))
    a3 = [x for x in a if a.count(x) == 3]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 3 and len(a1) == 4 and sum(a3)/3 > sum(a)/7:
        print(k)
    k += 1
print(k)
#16001 хуйня строчка ее нету в файле гн ебнутый код